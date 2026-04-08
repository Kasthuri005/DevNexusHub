from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Show these fields in the admin list view
    search_fields = ('title', 'content')  # Enable search functionality

admin.site.register(Review, ReviewAdmin)
