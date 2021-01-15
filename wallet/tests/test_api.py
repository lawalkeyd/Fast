from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restless.exceptions import Unauthorized, BadRequest 


from users.tests.factories import UserssFactory
from .factories import WalletFactory


class NoobWalletAPITestCase(TestCase):
      def setUp(self):
          self.user = UserssFactory()
          self.user.is_noob = True
          self.user.main_currency = 'CAD'
          self.user.save()
          self.wallet = WalletFactory(user=self.user)
          self.wallet.save()
          self.client.login(username=self.user.username, password=self.user.password)          

      def test_wallet_list(self):
          """GET the list of Wallets"""
          response = self.client.get(reverse('api_wallet_list'))
          self.assertEqual(response.status_code, 200)

      def test_wallet_detail(self):
          """GET details for User's wwallet."""
          response = self.client.get(reverse('api_wallet_detail', kwargs={'pk': self.wallet.pk}))
          self.assertEqual(response.status_code, 200)
