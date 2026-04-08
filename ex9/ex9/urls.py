from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Product listing page
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Add product to cart
    path('cart/', views.cart, name='cart'),  # View cart page
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  # Remove from cart
]
