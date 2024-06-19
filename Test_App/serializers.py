from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')

        if password != password2:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'



