import django_filters
from .models import Note
from django_filters import CharFilter,ChoiceFilter


class NoteFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr='icontains')
    # semester = ChoiceFilter(field_name='semester')
    # department = ChoiceFilter(field_name='department')
    class Meta:
        model = Note
        fields = ['department','semester','title']