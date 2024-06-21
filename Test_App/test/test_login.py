import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
def test_user(api_client):
    url=reverse('user-register')
    data={
        "username":"arun34",
        "password":"12",
        "password2":"12"
    }
    response=api_client.post(url,data,format='json')
    print(response.data)
    assert response.status_code ==201

@pytest.mark.django_db
# @pytest.mark.skipif
# @pytest.mark.xfail(reason="user name not yet")
def test_login(api_client,create_user):
    username = 'njnd'
    password = '1234'
    user = create_user(username=username, password=password)
    assert User.objects.filter(username=user.username).exists()
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
    url=reverse('user-get')
    response=api_client.get(url)
    print(response.data)
    assert response.status_code == 200
    assert len(response.data) == 4

