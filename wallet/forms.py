from django import forms
from .models import Wallet
from users.models import currency_choices

class FundsForm(forms.Form):
    amount= forms.FloatField()
    currency = forms.ChoiceField(choices=currency_choices)