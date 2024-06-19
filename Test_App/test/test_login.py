# import pytest
# from django.urls import reverse
# from rest_framework.test import APIClient
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token


# @pytest.mark.django_db
# class TestPytest:

#     @pytest.fixture
#     def api_client(self):
#         return APIClient()

#     @pytest.fixture
#     def create_user(self):
#         def make_user(**kwargs):
#             return User.objects.create_user(**kwargs)
#         return make_user

#     # def test_user(self,api_client):
#     #     url=reverse('user-register')
#     #     data={
#     #         "username":"arun",
#     #         "password":"12",
#     #         "password2":"12"
#     #     }
#     #     response=api_client.post(url,data,format='json')
#     #     print(response.status_code)
#     #     assert response.status_code ==201


#     def test_login(self,api_client, create_user):
#         username = 'arun'
#         password = '12345'
#         user = create_user(username=username, password=password)
#         print(user)

#         # Ensure the user is created in the database
#         assert User.objects.filter(username=user.username).exists()

#         # Define the login URL
#         url = reverse('user-login')

#         # Test successful login
#         data = {'username': username, 'password': password}
#         response = api_client.post(url, data, format='json')
#         assert response.status_code == 200
#         assert 'token' in response.data

#         # # Test failed login with incorrect credentials
#         data_invalid = {'username': username, 'password': 'wrongpassword'}
#         response_invalid = api_client.post(url, data_invalid, format='json')
        
#         print(response_invalid.status_code)
#         print(response_invalid.data)

#         # Assertions for a failed login
#         assert response_invalid.status_code == 400
#         assert 'token' not in response_invalid.data

#     # def test_logout(self,api_client,create_user):
#     #     user=create_user(username="arun",password="1234")
#     #     token=Token.objects.create(user=user)
#     #     api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
#     #     url=reverse('user-logout')
#     #     response=api_client.post(url)
#     #     assert response.status_code == 200

#     # def test_student(self,api_client):
#     #     url=reverse('student')
#     #     response=api_client.delete(url)
#     #     print(response.status_code)
#     #     assert response.status_code == 200



