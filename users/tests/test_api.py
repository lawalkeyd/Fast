from django.test import TestCase
from django.urls import reverse
from django.test import Client


from users.tests.factories import UserssFactory


class NoobUserAPITestCase(TestCase):
      def setUp(self):
          self.user = UserssFactory()
          self.user.pk = 1
          self.user.is_noob = True
          self.user.main_currency = 'CAD'
          self.user.save()
          self.client.login(username=self.user.username, password=self.user.password)

      def test_get_list(self):
          """GET the list of Users"""

          response = self.client.get(reverse('api_user_list'))
          self.assertEqual(response.status_code, 200)

      def test_get_detail(self):
          """GET details for User."""
          response = self.client.get(reverse('admin_user', kwargs={'pk': 1}))
          self.assertEqual(response.status_code, 401)

class AdminAPITestCase(TestCase):
      def setUp(self):
          self.user = UserssFactory()
          self.user.is_staff = True
          self.user.is_superuser = True
          self.user.save()
          self.client = Client()
          self.client.login(username=self.user.username, password=self.user.password)

      def test_is_authenticated(self):
          self.assertEqual(self.user.is_authenticated, True)

      def test_is_superuser(self):
          self.assertEqual(self.user.is_superuser, True)              

      def test_get_list(self):
          """GET the list of Users"""
          response = self.client.get(reverse('admin_user'))
          self.assertEqual(response.status_code, 200)

    #   def test_get_detail(self):
    #       """GET details for User."""
    #       response = self.client.get(reverse('admin_wallet', kwargs={'pk': 1}))
    #       self.assertEqual(response.status_code, 200)

class ClientAPITestCase(TestCase):
      def setUp(self):
          self.user = UserssFactory()
          self.user.is_noob = True
          self.user.save()
          self.client.login(username=self.user.username, password=self.user.password)
                    
      def test_is_authenticated(self):
          self.assertEqual(self.user.is_authenticated, True)

      def test_is_logged_in(self):
          self.client.post('login', {'username': self.user.username, 'password': self.user.password})
          self.assertEqual(self.user.is_superuser, False)  

      def test_is_noob(self):
          self.assertEqual(self.user.is_noob, True)                        




