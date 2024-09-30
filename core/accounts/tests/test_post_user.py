import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import User
from datetime import datetime

@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.mark.django_db
class TestUserApi:
    def test_create_user_status_201(self,api_client):
        url = reverse('account:api-v1:registration')
        data ={
            'email':'test1@gmail.com',
            'password':'1234qwer@',
            'password1':'1234qwer@',
        }
        response = api_client.post(url,data=data,format='json')
        print(response.data)
        assert response.status_code == 201
        assert User.objects.filter(email=data["email"]).exists()
