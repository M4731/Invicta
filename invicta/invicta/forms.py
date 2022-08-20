from django import forms
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    name = forms.CharField()
    email = forms.EmailField()

    def send_email(self):
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']

        send_mail(
            name + " contact mail",
            message + "\ncontact email: " + email,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )