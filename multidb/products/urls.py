from django.conf.urls import url

from . import views

app_name = "products"
urlpatterns = [
    url(regex=r"^$", view=views.ProductList.as_view(), name="list"),
    url(regex=r"^create/$", view=views.ProductCreate.as_view(), name="create"),
    url(regex=r"^(?P<db>[\w.@+-]+)/update/(?P<pk>\d+)/$", view=views.ProductUpdate.as_view(), name="update"),
    url(regex=r"^(?P<db>[\w.@+-]+)/delete/(?P<pk>\d+)/$", view=views.ProductDelete.as_view(), name="delete"),
]
