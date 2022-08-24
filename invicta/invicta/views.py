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
    
class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class ThanksContactPage(TemplateView):
    template_name = 'thanks_contact.html'

class TeacherFilter(django_filters.FilterSet):

    class Meta:
        model = Teacher
        fields = ['subject']

@method_decorator([login_required], name='dispatch')
class ListTeachers(FilterView):
    model = Teacher
    template_name = 'all_teachers.html'
    filterset_class = TeacherFilter

class ContactFormView(generic.FormView):
    template_name = 'contact_page.html'
    form_class = ContactForm
    # success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('thanks_contact')