from django.contrib import admin
from django.urls import path
from miniapp.views import review_list, review_detail, review_create, review_delete

urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line for admin page
    path('', review_list, name='review_list'),
    path('review/<int:pk>/', review_detail, name='review_detail'),
    path('review/new/', review_create, name='review_create'),
    path('review/<int:pk>/delete/', review_delete, name='review_delete'),
]
