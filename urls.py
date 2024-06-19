
from django.urls import path
from . import views

app_name = "ecommerce"

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
]