# import pytest
# from Test_App.models import Student
# from rest_framework.test import APIClient
# from django.urls import reverse



# @pytest.mark.django_db
# class TestStudent:

#     @pytest.fixture
#     def api_client(self):
#         return APIClient()

#     @pytest.fixture
#     def student_create_payload(self):
#         payload={
#             "name":"arun",
#             "age":"23",
#             "dept":"ECE",
#             "email":"arun@gmail.com"
#         }
#         record=Student.objects.create(**payload)
#         return record 

#     @pytest.fixture
#     def student_payload(self):
#         payload={
#             "name":"arun",
#             "age":"23",
#             "dept":"ECE",
#             "email":"arun@gmail.com"
#         }

#         return payload


#     def test_student(self,api_client,student_payload):
#         url=('/student/post/')
#         response=api_client.post(url,student_payload,format='json')
#         print(response.data,"***************************************************")
#         assert response.status_code == 201
#         assert Student.objects.count() == 1

#     def test_get(self,api_client,student_create_payload):
#         url=('student-get')
#         response=api_client.get(reverse(url))
#         print(response.data,"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#         assert response.status_code==200
#         assert len(response.data)==1

#         data= dict(response.data[0])
#         assert data['age'] == 23

#     def test_update(self,student_create_payload,api_client,student_payload):
#         url=(f'/student/update/{student_create_payload.id}/')
#         response=api_client.put(url,student_payload)
#         print(response.data,"###############################################")
#         assert response.status_code == 200
#         print(student_create_payload.id)

