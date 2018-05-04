from django.db.models import Value, CharField
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Product
from multidb.users.models import User
from .forms import ProductForm


class ProductCreate(LoginRequiredMixin, CreateView):
    template_name = 'product/create.html'
    model = Product
    form_class = ProductForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        instance = form.save(commit=False)
        instance.user = request.user.id
        database = request.POST['database']
        instance.save(using=database)
        return redirect(reverse("products:list"))

    def get_context_data(self, **kwargs):
        ctx = super(ProductCreate, self).get_context_data(**kwargs)
        databases = self.request.user.databases.all()
        ctx['databases'] = databases
        return ctx


class ProductList(LoginRequiredMixin, ListView):
    template_name = 'product/list.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dbs = self.request.user.databases.all()
        product_list = []
        for d in dbs:
            products = Product.objects.using(d.name).filter(user=self.request.user.id).values('id', 'name', 'description').annotate(db=Value(d.name, output_field=CharField()))
            product_list.extend(products)
        context['product_list'] = product_list
        return context


class ProductUpdate(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        instance = Product.objects.using(kwargs['db']).get(pk=kwargs['pk'])
        instance.name = request.POST['name']
        instance.description = request.POST['description']
        instance.save(using=kwargs['db'])
        return redirect(reverse("products:list"))

    def get(self, request, *args, **kwargs):
        instance = Product.objects.using(kwargs['db']).get(pk=kwargs['pk'])
        form = ProductForm(initial={'name': instance.name, 'description':instance.description})
        return render(request, 'product/update.html', {'form': form})


class ProductDelete(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        instance = Product.objects.using(kwargs['db']).get(pk=kwargs['pk'])
        instance.delete(using=kwargs['db'])
        return redirect(reverse("products:list"))

