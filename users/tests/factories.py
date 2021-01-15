from factory import django, Faker

from ..models import Userss


class UserssFactory(django.DjangoModelFactory):
    username = Faker('first_name')
    password = 'james2234'

    class Meta:
        model = Userss