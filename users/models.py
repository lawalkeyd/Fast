from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

currency_choices=  [
    ('AUD', 'Australian Dollar'),
    ('CAD', 'Canadian Dollar'),
    ('GBP', 'British Pound'),
    ('USD', 'US Dollar'),
    ('JPY', 'Janpanese Yen'),
]
class Userss(AbstractUser):
    is_noob = models.BooleanField(default=False)
    is_elite = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    main_currency = models.CharField(choices=currency_choices, max_length=3, blank=True, null=True)

class ClientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    

    def __str__(self):
        return self.user.username