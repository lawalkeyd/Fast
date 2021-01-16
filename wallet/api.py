from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from restless.exceptions import Unauthorized, BadRequest 

from users.models import Userss
from .models import Wallet
from .forms import FundsForm
import requests

class ClientFund(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'currency': 'currency',
        'client_username': 'user.username',
        'current_amout': 'amount'
    })

    #def is_authenticated(self):
        #return self.request.user.is_authenticated()

    def list(self):
        if self.request.user.is_authenticated == False:
            raise Unauthorized('You are not logged in')
        return Wallet.objects.all()

    def detail(self, pk):
        try:
            wallet = Wallet.objects.get(id=pk)
        except wallet.DoesNotExist:
            raise BadRequest('Something is wrong.')
        return wallet
      

class FundWallet(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'amount': 'amount',
        'currency': 'currency', 
    })

    def is_authenticated(self):
        return self.request.user.is_authenticated and (self.request.user.is_noob or self.request.user.is_elite)
      
    def create(self):
        form = FundsForm(self.data)
        if not form.is_valid():
            raise BadRequest('Something is wrong.')
        amount=form.cleaned_data['amount']
        currency=form.cleaned_data['currency']
        if self.request.user.is_noob:
            if currency == self.request.user.main_currency:
                wallet, created = Wallet.object.get_or_create(
                    currency=currency,
                    user = self.request.user,
                )
                wallet.amount += amount
                wallet.save()
                return wallet
            elif currency != self.request.user.main_currency:
                r = requests.get('https://data.fixer.io/api/latest/?{{API_KEY}}&{{self.user.main_currency}}', params=request.GET)
                if r.success == True:
                    rate = r.rates[currency]
                    wallet,created = Wallet.object.get_or_create(
                        currency=currency,
                        user = self.request.user,
                    )
                    wallet.amount += amount * rate
                    wallet.save()
                    return wallet
                else:
                    raise BadRequest('Something is wrong.')
            else:
                raise BadRequest('Something is wrong.')      
        if self.request.user.is_elite:
            wallet, created = Wallet.object.get_or_create(
                currency=currency,
                user = self.request.user,
            )
            wallet.amount += amount
            wallet.save()
            return wallet   
        
class WithdrawWallet(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'amount': 'amount',
        'currency': 'currency', 
    })

    def is_authenticated(self):
        return self.request.user.is_authenticated and (self.request.user.is_noob or self.request.user.is_elite)
      
    def create(self):
        form = FundsForm(self.data)
        if not form.is_valid():
            raise BadRequest('Something is wrong.')
        amount=form.cleaned_data['amount']
        currency=form.cleaned_data['currency']
        if self.request.user.is_noob:
            if currency == self.user.main_currency:
                wallet, created = Wallet.object.get(
                    currency=currency,
                    user = self.request.user,
                )
                if amount > wallet.amount:
                    raise BadRequest('You do not have sufficient funds')
                wallet.amount -= amount
                wallet.save()
                return wallet
            elif currency != self.request.user.main_currency:
                r = requests.get('https://data.fixer.io/api/latest/?{{API_KEY}}&{{self.user.main_currency}}')
                if r.success == True:
                    rate = r.rates[currency]
                    wallet,created = Wallet.object.get_or_create(
                        currency=currency,
                        user = self.request.user,
                    )
                    new_amount = amount * rate
                    if wallet.amount < new_amount:
                        raise BadRequest('You do not have sufficient funds')
                    wallet.amount -= new_amount
                    wallet.save()
                    return wallet
                else:
                    raise BadRequest('Something is wrong.')
            else:
                raise BadRequest('Something is wrong.')      
        if self.request.user.is_elite:
            try:
                wallet = Wallet.object.get(
                    currency=currency,
                    user = self.request.user,
                )
            except:
                wallet = Wallet.objects.get(user=self.request.user, currency=self.request.user.main_currency)
                if currency != self.request.user.main_currency:
                    r = requests.get('https://data.fixer.io/api/latest/?{{API_KEY}}&{{self.user.main_currency}}')
                    if r.success == True:
                        rate = r.rates[currency]
                        wallet,created = Wallet.object.get_or_create(
                            currency=currency,
                            user = self.request.user,
                        )
                        new_amount = amount * rate
                        if wallet.amount < new_amount:
                            raise BadRequest('You do not have sufficient funds')
                    else:
                        raise BadRequest('Something is wrong.')                               
                wallet.amount -= amount
                wallet.save()
                return wallet   
         



