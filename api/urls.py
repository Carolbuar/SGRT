from django.urls import path
from . import views

urlpatterns = [
    path("customers_list/", views.customers_list, name="customers_list"),
    path("add_customer/", views.add_customer, name="add_customer"),  
]