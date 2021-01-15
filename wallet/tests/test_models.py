from django.test import TestCase

from users.tests.factories import UserssFactory
from .factories import WalletFactory


class UserssTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        user = UserssFactory()
        wallet = WalletFactory(user=user)
        self.assertEqual(str(wallet), user.username + ' in ' + wallet.currency)