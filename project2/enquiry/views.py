from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import EnquiryForm

def enquiry_view(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                subject=f"Enquiry from {name}",
                message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['manikasthuri2019@gmail.com'],  # Change this to your email
            )
            
            return render(request, 'enquiry/success.html')  # Redirect to success page
    else:
        form = EnquiryForm()
    
    return render(request, 'enquiry/enquiry_form.html', {'form': form})
