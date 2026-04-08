from django.urls import path
from app4 import views

urlpatterns = [
    path('', views.feedback_view, name='feedback_form'),
    path('feedback/list/', views.feedback_list, name='feedback_list'),
]