from django.views.generic import TemplateView
from accounts.models import Teacher
from django.views import generic
import django_filters
from django_filters.views import FilterView
from invicta.forms import ContactForm
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomePage(TemplateView):
    template_name = 'index.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = ['subject']

@method_decorator([login_required], name='dispatch')
class ListTeachers(FilterView):
    model = Teacher
    template_name = 'all_teachers.html'
    filterset_class = TeacherFilter
    paginate_by = 5

class ContactFormView(generic.FormView):
    template_name = 'contact_page.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('thanks_contact')

class ThanksContactPage(TemplateView):
    template_name = 'thanks_contact.html'