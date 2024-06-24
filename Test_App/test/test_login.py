import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token

@pytest.mark.django_db
def test_user_create(api_client):
    url=reverse('user-register')
    data={
        "username":"giri",
        "password":"12",
        "password2":"12",
        "email":"Arun@gmail.com",
    }
    response=api_client.post(url,data,format='json')
    print(response.data)
    assert response.status_code ==201
    print(response.status_code)

@pytest.mark.django_db
def test_login(api_client,create_user):
    username = 'santhosh'
    password = '1234'
    user = create_user(username=username, password=password)
    url = reverse('user-login')

    # Test successful login
    data = {'username': username, 'password': password}
    response = api_client.post(url, data, format='json')
    print(response.data)
    print(response.status_code)
    assert response.status_code == 200
    assert 'token' in response.data

    # Test failed login with incorrect credentials
    data_invalid = {'username': username, 'password': 'wrongpassword'}
    response_invalid = api_client.post(url, data_invalid, format='json')
    
    print(response_invalid.status_code)
    print(response_invalid.data)

    # Assertions for a failed login
    assert response_invalid.status_code == 400
    assert 'token' not in response_invalid.data


# @pytest.mark.skip(reason="This test is skipped")
@pytest.mark.django_db
def test_logout(api_client,create_user):
    user=create_user(username="arun33",password="1234")
    token=Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    url=reverse('user-logout')
    response=api_client.post(url)
    print(response.data)
    assert response.status_code == 200



@pytest.mark.django_db
def test_get_user(api_client,create_user):
    user=create_user(username="arun34",password='1234')
    token=Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    url=reverse('user-details')
    response=api_client.get(url)
    print(response.data)
    assert response.status_code == 200
    assert len(response.data) == 4


@pytest.mark.django_db
def test_user_delete(api_client):
    user = User.objects.create_user(username='testuser', password='testpassword')
    url=reverse('user-delete',kwargs={'pk':user.pk})
    response=api_client.delete(url)
    print(response.data)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not User.objects.filter(pk=user.pk).exists()


