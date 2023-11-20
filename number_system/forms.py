from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from .models import Profile


class BaseConversionForm(forms.Form):
    source_base = forms.IntegerField(label='Source Base')
    target_base = forms.IntegerField(label='Target Base')
    input_number = forms.CharField(label='Input Number')


class BaseCalculatorForm(forms.Form):
    target_base = forms.IntegerField(label='Target Base')
    input_expression = forms.CharField(label='Input Expression', widget=forms.TextInput(attrs={'id': 'latex-input'}))


class AnswerSubmissionForm(forms.Form):
    user_answer = forms.CharField()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2']


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']