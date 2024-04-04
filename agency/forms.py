from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Topic, Newspaper, Redactor


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class NewspaperForm(forms.ModelForm):
    redactors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Newspaper
        fields = ['title', 'content', 'published_date', 'topics', 'redactors']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class RedactorForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ['username', 'first_name', 'last_name', 'email', 'years_of_experience', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        redactor = super().save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            redactor.set_password(password)
        if commit:
            redactor.save()
        return redactor


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Redactor
        fields = ('username', 'email', 'password1', 'password2')
