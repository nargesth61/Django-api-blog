import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import User
from datetime import datetime

@pytest.fixture
def api_client():
    client = APIClient()
    return client
@pytest.fixture
def user():
    user = User.objects.create_user(email='test@gmail.com',password='1234qwer',is_verified=True)
    return user


@pytest.mark.django_db
class TestPoatApi:
    def test_get_post_response_200_status(self,api_client,user):
        url = reverse('blog:api:post-list')
        api_client.force_login(user=user)
        response = api_client.get(url)
        assert response.status_code == 200
    
    def test_create_post_response_201_status(self,api_client,user):
        url = reverse('blog:api:post-list')
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        api_client.force_login(user=user)

        response = api_client.post(url,data=data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(
        self, api_client, user
    ):
        url = reverse("blog:api:post-list")
        data = {"title": "test", "content": "description"}
        user = user

        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400