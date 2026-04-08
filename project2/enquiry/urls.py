from django.urls import path
from .views import enquiry_view

urlpatterns = [
    path('', enquiry_view, name='enquiry'),
]
