from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

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
        

class LoginLogoutTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="example", password="newpasswprd@123")
    
    def test_login(self):
        data = {
            "username": "example",
            "password": "newpasswprd@123"
        }
        response = self.client.post(reverse("login"), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
