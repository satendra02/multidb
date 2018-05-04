from django import forms

from .models import Product
from multidb.users.models import User


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description',)

