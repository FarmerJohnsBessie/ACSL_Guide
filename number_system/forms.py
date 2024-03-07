from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
    user_answer = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'pg-submit-input col-6', 'placeholder':'Enter your answer'}))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['username'].widget.attrs = {'class':'login-text', 'placeholder':'Enter your username'}
        self.fields['email'].label = ""
        self.fields['email'].widget.attrs = {'class': 'login-text', 'placeholder': 'Enter your email'}
        self.fields['password1'].label = ""
        self.fields['password1'].widget.attrs = {'class': 'login-text', 'placeholder': 'Enter your password again'}
        self.fields['password2'].label = ""
        self.fields['password2'].widget.attrs = {'class': 'login-text', 'placeholder': 'Enter your password again'}
        self.fields['first_name'].label = ""
        self.fields['first_name'].widget.attrs = {'class': 'login-text', 'placeholder': 'Enter your first name'}
        self.fields['last_name'].label = ""
        self.fields['last_name'].widget.attrs = {'class': 'login-text', 'placeholder': 'Enter your last name'}
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

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


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['username'].widget.attrs = {'class':'login-text', 'placeholder':'Enter your username'}

        self.fields['password'].label = ""
        self.fields['password'].widget.attrs = {'class': 'login-text', 'placeholder': 'Enter your password'}