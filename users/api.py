from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from restless.exceptions import Unauthorized, BadRequest 

from .models import Userss
from .forms import UserForm
from wallet.models import Wallet

class UserResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'client_username': 'username',
        'is_noob': 'is_noob',
        'is_elite': 'is_elite',
        'is_admin': 'admin',
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
    

class AdminResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'admin_username': 'username',
        'is_admin': 'is_admin',
        'is_noob': 'is_noob',
        'is_elite': 'is_elite',        
    })

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
            is_admin= True) 
    
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
        'is_admin': 'is_admin',
        'is_noob': 'is_noob',
        'is_elite': 'is_elite',        
    })

    def is_authenticated(self):
        return self.user.is_authenticated and (self.user.is_noob or self.user.is_elite)

    def detail(self, pk):
        try:
            user = Userss.objects.get(id=pk)
        except user.DoesNotExist:
            raise BadRequest('Something is wrong.')
        return user
            
        