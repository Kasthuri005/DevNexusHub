from django.urls import path
from app import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('items/', views.items_view, name='items'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<str:item>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<str:item>/', views.remove_from_cart, name='remove_from_cart'),
    path('admin/', admin.site.urls),
]
