from django import forms

class AnswerForm(forms.Form):
    value = forms.CharField(label='Answer', max_length=1000)
