from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, Teacher, Subject
from django import forms

class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name", "phone_number", "email", "password1", "password2")
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["first_name"].label = "First Name"
        self.fields["last_name"].label = "Last Name"
        self.fields["email"].label = "Email Address"
        self.fields["phone_number"].label = "Phone Number"

class TeacherSignUpForm(UserCreationForm):
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all()
    )

    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name", "phone_number", "email", "password1", "password2")
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()

        teacher = Teacher.objects.create(user=user)
        teacher.subject = self.cleaned_data.get('subject')
        teacher.save()

        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["first_name"].label = "First Name"
        self.fields["last_name"].label = "Last Name"
        self.fields["email"].label = "Email Address"
        self.fields["phone_number"].label = "Phone Number"