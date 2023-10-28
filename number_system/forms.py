from django import forms

class BaseConversionForm(forms.Form):
    source_base = forms.IntegerField(label='Source Base')
    target_base = forms.IntegerField(label='Target Base')
    input_number = forms.CharField(label='Input Number')

class BaseCalculatorForm(forms.Form):
    target_base = forms.IntegerField(label='Target Base')
    input_expression = forms.CharField(label='Input Expression', widget=forms.TextInput(attrs={'id': 'latex-input'}))

class AnswerSubmissionForm(forms.Form):
    user_answer = forms.IntegerField()
