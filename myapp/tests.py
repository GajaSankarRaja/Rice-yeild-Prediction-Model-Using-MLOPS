from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UserInput

class UserInputTests(APITestCase):
    def test_create_user_input(self):
        url = reverse('userinput-list')
        data = {'input1': 'value1', 'input2': 'value2'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserInput.objects.count(), 1)
        self.assertEqual(UserInput.objects.get().input1, 'value1')
        self.assertEqual(UserInput.objects.get().input2, 'value2')
