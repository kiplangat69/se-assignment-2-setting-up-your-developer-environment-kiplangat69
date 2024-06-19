from django.shortcuts import render
from .models import product, customer

# Create your views here.
# ecommerce/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def product_list(reguest):
    products = Product.objects.all()

     return render(request, 'ecommerce/product_list.html', {'products': products})

def product_detail(request, product_id):
   product = get_object_or_404(Product, pk=product_id)

   return render(request, 'ecommerce/product_detail.html', {'product': product})
   
   def customer_list(request):
    customer = Customer.objects.all()  # Retrieve all customers from the database
    return render(request, 'ecommerce/customer_list.html', {'customers': customers})
   
   def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)  # Retrieve customer object or 404 if not found
    return render(request, 'ecommerce/customer_detail.html', {'customer': customer})

