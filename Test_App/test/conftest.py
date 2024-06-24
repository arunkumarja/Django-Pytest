import pytest
from rest_framework.test import  APIClient
from django.contrib.auth.models import User
from django.core.management import call_command

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    def user(**kwargs):
        return User.objects.create_user(**kwargs)
    return user


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'data.json')