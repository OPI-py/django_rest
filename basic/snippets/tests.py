from django.test import TestCase
from rest_framework.test import APIClient


client = APIClient()
client.login(username='test', password='test123')