from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    birth_date = models.DateField()



class User_Data(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE).primary_key
    email = models.EmailField()
    password = models.CharField(max_length=255)
    account_type = models.IntegerField()


class Passport(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE).primary_key
    passport_numbers = models.IntegerField()
    passport_organ = models.CharField(max_length=255)
    issue_date = models.DateField()
    subdivision_code = models.CharField(max_length=10)


class Parents(models.Model):
    parent = models.ForeignKey('Users', on_delete=models.CASCADE).primary_key
    privileges = models.ForeignKey('Parent_Privileges', on_delete=models.CASCADE)


class Parent_Privileges(models.Model):
    type = models.CharField(max_length=255)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    access = models.IntegerField()


class Teacher(models.Model):
    teacher = models.ForeignKey('Users', on_delete=models.CASCADE).primary_key
    qualification = models.FileField()
    institution = models.CharField(max_length=255)
    diploma = models.CharField(max_length=255)


class Children(models.Model):
    child = models.ForeignKey('Users', on_delete=models.CASCADE).primary_key
    rating = models.IntegerField()