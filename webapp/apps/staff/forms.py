from django import forms

class NewUserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', max_length=100,
               widget=forms.PasswordInput)
    last_name = forms.CharField(label='Last name', max_length=100)
    first_name = forms.CharField(label='First name', max_length=100)
