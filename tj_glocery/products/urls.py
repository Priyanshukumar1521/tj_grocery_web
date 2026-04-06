from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('', views.product_list, name='shop'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]