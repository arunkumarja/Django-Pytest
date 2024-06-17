# test_create_student_api.py

import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from Test_App.models import Student  # Adjust based on your app structure

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
class TestStudentAPI:

    def test_create_student(self, api_client):
        url = reverse('student_post')  # Assuming 'student-create' is your URL name for creating students
        
        # Data to be sent in the POST request
        data = {
            'name': 'John Doe',
            'age': 25,
            'dept':'EEE',
            'email':"a@gmail.com"
        }

        # Perform a POST request using the client
        response = api_client.post(url, data)

        # Assert that the response status code is 201 (created)
        assert response.status_code == status.HTTP_201_CREATED

        # Optionally, you can check the response JSON content
        print(response.json())
