from django import forms
from .models import Userss

class UserForm(forms.ModelForm):
    class Meta(object):
        model = Userss
        fields = ['username', 'main_currency', 'is_noob', 'is_elite']