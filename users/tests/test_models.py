from django.test import TestCase

from ..models import Userss
from .factories import UserssFactory


class UserssTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        user = UserssFactory()
        self.assertEqual(str(user), user.username)