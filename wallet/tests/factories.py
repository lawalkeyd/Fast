from factory import django, Faker
from ..models import Wallet
from users.models import Userss


class WalletFactory(django.DjangoModelFactory):
    currency = 'USD'
    amount = 10000
    class Meta:
        model = Wallet