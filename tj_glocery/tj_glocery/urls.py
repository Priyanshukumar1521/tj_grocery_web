from django.contrib import admin
from django.urls import path, include

# App Views
from products import views as product_views
from accounts import views as account_views
from cart import views as cart_views
from orders import views as order_views

# Media Files (Images show karne ke liye)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # =====================
    # ADMIN PANEL
    # =====================
    path('admin/', admin.site.urls),
    path('', include('products.urls')),

    # =====================
    # HOME + PRODUCTS
    # =====================
    path('', product_views.home, name='home'),
    path('shop/', product_views.shop, name='shop'),
    path('product/<int:id>/', product_views.product_detail, name='product'),

    # =====================
    # AUTHENTICATION
    # =====================
    path('login/', account_views.login_view, name='login'),
    path('register/', account_views.register_view, name='register'),
    path('logout/', account_views.logout_view, name='logout'),

    # =====================
    # CART
    # =====================
    path('cart/', cart_views.cart_page, name='cart'),

    # =====================
    # ORDER / CHECKOUT
    # =====================
    path('checkout/', order_views.checkout, name='checkout'),
]

# =====================
# MEDIA FILES SERVING
# =====================
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)