import pytest
from rest_framework.test import  APIClient
from django.contrib.auth.models import User
import os
from django.conf import settings

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)
    return make_user


@pytest.fixture(scope='session')
def django_db_set():
   settings.DATABASES['default']= {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('NAME'),  
        'USER': os.getenv('USER'),  
        'PASSWORD': os.getenv('PASSWORD'),  
        'HOST': os.getenv('HOST'),  
        'PORT': os.getenv('PORT'),  
    }


from django.core.management import call_command

@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'data.json')




# from django.test.utils import setup_databases, teardown_databases

# @pytest.fixture(scope='session', autouse=True)
# def setup_and_teardown_db():
#     # Setup the test databases
#     old_config = setup_databases(verbosity=1, interactive=False, keepdb=False)
#     yield
#     # Teardown the test databases
#     teardown_databases(old_config, verbosity=1)        