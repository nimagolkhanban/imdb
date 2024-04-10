from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token


# Create your tests here.
class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "username": "testcase",
            "password": "testcase@test123",
            "password2": "testcase@test123",
            "email": "test@test.com"
        }
        
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)