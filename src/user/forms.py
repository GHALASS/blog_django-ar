from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('username', 'email', 'first_name',
            'last_name', 'password')
