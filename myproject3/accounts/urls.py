from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='admin'),
    path('home/', views.home, name='home'),
path('restricted/', views.restricted_view, name='restricted_page')
]
