from rest_framework import serializers
from main.models import User, User_Data, Teacher_Users

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
    account_type = serializers.IntegerField()
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    

class UserDataSerializer(serializers.Serializer):
    user_id = User.user_id
    sex = serializers.CharField(max_length=15)
    name = serializers.CharField(max_length=255)
    surname = serializers.CharField(max_length=255)
    patronymic = serializers.CharField(max_length=255, blank=True)
    
    def create(self, validated_data):
        return User_Data.objects.create(**validated_data)


class PassportSerializer(serializers.Serializer):
    user = User.user_id
    passport_numbers = serializers.IntegerField()
    passport_organ = serializers.CharField(max_length=255)
    issue_date = serializers.DateField()
    subdivision_code = serializers.CharField(max_length=10)
    birth_date = serializers.DateField()
    
    def create(self, validated_data):
        return Passport.objects.create(**validated_data)


class TeacherSerializer(serializers.Serializer):
    teacher = User.user_id
    qualification = serializers.FileField()
    institution = serializers.CharField(max_length=255)
    diploma = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        return Teacher_Users.objects.create(**validated_data)
    