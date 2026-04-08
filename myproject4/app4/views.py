from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
from .filters import FeedbackFilter

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback/list/')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

def feedback_list(request):
    feedbacks = Feedback.objects.all()
    feedback_filter = FeedbackFilter(request.GET, queryset=feedbacks)
    return render(request, 'feedback_list.html', {'filter': feedback_filter})


