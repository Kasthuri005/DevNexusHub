from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'review_detail.html', {'review': review})

def review_create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})

def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        review.delete()
        return redirect('review_list')
    return render(request, 'review_confirm_delete.html', {'review': review})
