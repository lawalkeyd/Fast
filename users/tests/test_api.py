from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restless.exceptions import Unauthorized, BadRequest 


from .factories import UserssFactory


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
          response = self.client.get(reverse('api_client_detail', kwargs={'pk': self.user.pk}))
          self.assertEqual(response.status_code, 200)

class AdminAPITestCase(TestCase):
      def setUp(self):
          self.user = UserssFactory()
          self.user.is_admin = True
          self.user.save()
          self.client.login(username=self.user.username, password=self.user.password)

      def test_is_authenticated(self):
          self.assertEqual(self.user.is_authenticated, True)

      def test_is_admin(self):
          self.assertEqual(self.user.is_admin, True)              

      def test_get_list(self):
          """GET the list of Users"""
          response = self.client.get(reverse('api_user_list'))
          self.assertEqual(response.status_code, 200)

      def test_get_detail(self):
          """GET details for User."""
          response = self.client.get(reverse('api_admin_detail', kwargs={'pk': 1}))
          self.assertEqual(response.status_code, 200)

class ClientAPITestCase(TestCase):
      def setUp(self):
          self.user = UserssFactory()
          self.user.is_noob = True
          self.user.save()
          self.client.login(username=self.user.username, password=self.user.password)

      def test_is_authenticated(self):
          self.assertEqual(self.user.is_authenticated, True)

      def test_is_admin(self):
          self.assertEqual(self.user.is_admin, False)              

      def test_get_detail(self):
          """GET details for User."""
          response = self.client.get(reverse('api_client_detail', kwargs={'pk': self.user.pk}))
          self.assertEqual(response.status_code, 200)


