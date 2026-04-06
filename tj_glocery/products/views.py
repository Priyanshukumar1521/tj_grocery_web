from django.shortcuts import render
from .models import Product


# HOME PAGE (Products show honge)
from .models import Product

def home(request):
    products = Product.objects.all()[:8]   # featured products
    return render(request,'index.html',{
        'products':products
    })
    
# SHOP PAGE
def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

# PRODUCT DETAIL PAGE
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {'product': product})



def cart_view(request):
    products = Product.objects.all()
    return render(request, 'cart.html', {'products': products})

# CHECKOUT PAGE
def checkout(request):
    return render(request, 'checkout.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})