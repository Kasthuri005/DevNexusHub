import django_filters
from .models import Feedback

class FeedbackFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    event_rating = django_filters.ChoiceFilter(choices=[(i, i) for i in range(1, 6)], label='Event Rating')
    
    class Meta:
        model = Feedback
        fields = ['name', 'event_rating']