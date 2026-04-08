from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'accounts/home.html')

@login_required
def restricted_view(request):
    return render(request, 'accounts/restricted_page.html') 
def admin(request):
    return render(request, 'admin.py')