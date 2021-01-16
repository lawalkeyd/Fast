from django.test import TestCase
from django.urls import reverse
from restless.exceptions import Unauthorized, BadRequest 


from users.tests.factories import UserssFactory
from .factories import WalletFactory
from wallet.models import Wallet


class NoobWalletAPITestCase(TestCase):
      def setUp(self):
          self.user = UserssFactory()
          self.user.is_noob = True
          self.user.main_currency = 'CAD'
          self.user.save()
          self.wallet = WalletFactory(user=self.user)
          self.wallet.save()
          self.client.login(username=self.user.username, password=self.user.password)          

      def test_is_authenticated(self):
          self.assertEqual(self.user.is_authenticated, True)

      def test_wallet_created(self):
          wallet = Wallet.objects.get(id=1)
          self.assertEqual(wallet.user.id, self.user.id)    

      def test_wallet_list(self):
          """GET the list of Wallets"""
          response = self.client.get(reverse('api_wallet_list'))
          self.assertEqual(response.status_code, 200)

      def test_wallet_detail(self):
          """GET details for User's wallet."""
          response = self.client.get(reverse('api_wallet_detail', kwargs={'pk': self.wallet.pk}))
          self.assertEqual(response.status_code, 200)

      def test_fund_wallet(self):
          response = self.client.post(reverse('Fund_Wallet', data={'amount': 10000, 'currency': 'CAD'}))
          self.assertEqual(response.status_code, 200)

