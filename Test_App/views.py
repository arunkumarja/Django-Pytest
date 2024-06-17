from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student

class StudentAPI(APIView):
    def post(self,request):
        try: 
            serializer = StudentSerializer(data=request.data.get("id"))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors) 
        except Exception as e:
            return Response({'error': str(e)}) 

    def get(self,request,pk):
        student_d=Student.objects.get(id=pk)
        serializer=StudentSerializer(student_d)
        return Response(serializer.data)

from rest_framework import generics
from Test_App.models import Student
from Test_App.serializers import StudentSerializer

class StudentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer