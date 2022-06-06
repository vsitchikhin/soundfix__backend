from rest_framework import serializers
from .models import Users, User_Data, Passport, Parents, Parent_Privileges, Teacher, Children

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'surname', 'patronymic', 'birth_date')


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Data
        fields = ('user', 'email', 'password', 'account_type')


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = ('user', 'passport_numbers', 'passport_organ',
                  'issue_date', 'subdivision_code')


class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = ('parent', 'privileges')


class ParentPrivelegesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent_Privileges
        fields = ('type', 'teacher', 'access')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('teacher', 'qualification', 'institution', 'diploma')


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = ('child', 'rating')