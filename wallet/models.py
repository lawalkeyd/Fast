from django.db import models
from users.models import currency_choices, Userss
# Create your models here.
        
class Wallet(models.Model):
    user = models.ForeignKey(Userss, on_delete=models.CASCADE)
    currency = models.CharField(choices=currency_choices,max_length=3)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ' in ' + self.currency        


class WithdrawRequest(models.Model):
    user = models.ForeignKey(Userss, on_delete=models.CASCADE)
    amount = models.FloatField()
    currency = models.CharField(choices=currency_choices, max_length=3)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + ' in ' + self.currency 
        