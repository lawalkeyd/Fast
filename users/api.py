from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from restless.exceptions import Unauthorized, BadRequest 
from django.contrib.auth import authenticate, login

from .models import Userss
from .forms import UserForm
from wallet.models import Wallet

class UserResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'username': 'username',
        'is_noob': 'is_noob',
        'is_elite': 'is_elite',
        'is_superuser': 'is_superuser',
        'main_currency': 'main_currency',
    })
      
    def create(self):
        form = UserForm(self.data)
        if not form.is_valid():
            raise BadRequest('Something is wrong.')
        user = Userss.objects.create(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            is_elite=form.cleaned_data['is_elite'],
            is_noob=form.cleaned_data['is_noob'],
            main_currency=form.cleaned_data['main_currency'],
        )
        Wallet.objects.create(user=user, currency=form.cleaned_data['main_currency'], amount=0.0)
        return user
    
class LoginUser(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'username': 'username',
        'is_superuser': 'is_superuser',
        'is_noob': 'is_noob',
        'is_elite': 'is_elite',        
    })

    def create(self):
        form = UserForm(self.data)
        username=form.cleaned_data['username'],
        password=form.cleaned_data['password'],        
        if not form.is_valid():
            raise BadRequest('Something is wrong.')
        user = authenticate(username=username, password=password)
        if user:
            login(user)
        return user        




class AdminResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'username': 'username',
        'is_superuser': 'is_superuser',
        'is_noob': 'is_noob',
        'is_elite': 'is_elite',        
    })

    def is_authenticated(self):
        '''
        User is authenticated and is an admin user
        '''
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def list(self):
        return Userss.objects.all()

    def detail(self, pk):
        try:
            user = Userss.objects.get(id=pk)
        except user.DoesNotExist:
            raise BadRequest('Something is wrong.')
        return user
      
    def create(self):
        form = UserForm(self.data)
        if not form.is_valid():
            raise BadRequest('Something is wrong.')
        return Userss.objects.create(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            is_superuser= True) 
    
    def update(self, pk):
        try:
            user = Userss.objects.get(id=pk)
        except user.DoesNotExist:
            raise BadRequest('Something is wrong.')    
        user.is_elite = self.data['is_elite']
        user.is_noob = self.data['is_noob']
        user.save()
        return user  


class ClientResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'client_username': 'username',
        'is_superuser': 'is_superuser',
        'is_noob': 'is_noob',
        'is_elite': 'is_elite',        
    })

    def is_authenticated(self):
        return self.request.user.is_authenticated and (self.request.user.is_noob or self.request.user.is_elite)

    def detail(self, pk):
        try:
            user = Userss.objects.get(id=pk)
        except user.DoesNotExist:
            raise BadRequest('Something is wrong.')
        return user
            
        