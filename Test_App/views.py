from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .serializers import UserSerializer,StudentSerializer,UserSerializer1
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': serializer.data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key,"user":user.username}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            request.user.auth_token.delete()
            logout(request)
            return Response("User logout",status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class Userget(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            user=User.objects.all()
            data=UserSerializer1(user,many=True)
            return Response(data.data,status=200)
        except Exception as e:
            return Response(f'{e}',status=400)   
class DeleteAPI(APIView):
    def delete(self,request,pk):
        try:
            user=User.objects.get(pk=pk)
            user.delete() 
            return Response('User successfully deleted',status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(f"{e}")           


class StudentAPI(APIView):
    def post(self,request):
        try:

            student=StudentSerializer(data=request.data)
            if student.is_valid():
                student.save()
                return Response(student.data,status=status.HTTP_201_CREATED)
            return Response(student.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(f'{e}',status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

class StudentgetAPI(APIView):    
    def get(self,request):
        try:
            user=Student.objects.all()
            student=StudentSerializer(user,many=True)
            return Response(student.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f'{e}',status=status.HTTP_400_BAD_REQUEST)


class StudentpostAPI(APIView):
    def put(self,request,pk):
        try:
            user=Student.objects.get(pk=pk)
            student=StudentSerializer(user,data=request.data)
            if student.is_valid():
                student.save()
                return Response("successfully updated",status=status.HTTP_200_OK)
            return Response(student.errors,status=status.HTTP_400_BAD_REQUEST)   
        except Exception as e:
            return Response(f'{e}',status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
            