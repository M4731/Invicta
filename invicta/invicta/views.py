from django.views.generic import TemplateView
from accounts.models import Teacher
from django.views import generic
import django_filters
from django_filters.views import FilterView

class HomePage(TemplateView):
    template_name = 'index.html'
    
class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class TeacherFilter(django_filters.FilterSet):

    class Meta:
        model = Teacher
        fields = ['subject']

class ListTeachers(FilterView):
    model = Teacher
    template_name = 'all_teachers.html'
    filterset_class = TeacherFilter