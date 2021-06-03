from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from users.tests.factories import UserssFactory
from wallet.tests.factories import WalletFactory
from wallet.models import Wallet


class NoobWalletAPITestCase(TestCase):
      def setUp(self):
          self.user = UserssFactory()
          self.user.is_elite = True
          self.user.is_noob = False
          self.user.main_currency = 'CAD'
          self.user.save()
          self.token = Token.objects.create(user=self.user)
          self.token.save()
          self.wallet = WalletFactory(user=self.user)
          self.wallet.save()
          self.client.login(username=self.user.username, password=self.user.password)          

      def test_is_authenticated(self):
          self.assertEqual(self.user.is_authenticated, True)

      def test_wallet_created(self):
          wallet = Wallet.objects.get(id=self.wallet.id)
          self.assertEqual(wallet.user.id, self.user.id)    

      def test_wallet_list(self):
          """GET the list of Wallets"""
          response = self.client.get(reverse('api_wallet_list'))
          self.assertEqual(response.status_code, 200)

      def test_wallet_detail(self):
          """GET details for User's wallet."""
          response = self.client.get(reverse('my_wallet_list', kwargs={'pk': self.wallet.pk}))
          self.assertEqual(response.status_code, 200)

      def test_fund_wallet(self):
          params = {'amount': 10000, 'currency': 'CAD', 'id': self.user.id,}
          response = self.client.post(reverse('client_fund'), params, HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
          self.assertEqual(response.status_code, 200)

      def test_withdraw_wallet(self):
          params = {'amount': 10000, 'currency': 'CAD'}
          response = self.client.post('client_withdraw', params)
          self.assertEqual(response.status_code, 200)

