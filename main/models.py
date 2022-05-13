from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField().primary_key
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    patronymic = models.CharField(max_length = 255, blank = True)
    

class User_Data(models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE).primary_key
    email = models.EmailField()
    password = models.CharField(max_length = 255)
    account_type = models.IntegerField()
    
    
class ParentUsers(models.Model):
    parent = models.ForeignKey('User', on_delete = models.CASCADE).primary_key
    
    
class Child_Users(models.Model):
    child = models.ForeignKey('User', on_delete = models.CASCADE).primary_key
    rating = models.IntegerField()
    
    
class Teacher_Users(models.Model):
    teacher = models.ForeignKey('User', on_delete = models.CASCADE).primary_key
    qualification = models.FileField()
    institution = models.CharField(max_length = 255)
    
    
class Passport(models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE).primary_key
    passport_numbers = models.IntegerField()
    passport_organ = models.CharField(max_length = 255)
    issue_date = models.DateField()
    subdivision_code = models.CharField(max_length = 10)
    birth_date = models.DateField(blank=True, null=True)
    
    
class Chat(models.Model):
    sender = models.ForeignKey('User', on_delete = models.CASCADE).primary_key
    recipient = models.ForeignKey('User', on_delete = models.CASCADE).primary_key
    message = models.TextField(blank = True)
    send_time = models.TimeField(auto_now_add = True)
    
    
class User_Activities(models.Model):
    activity_id = models.AutoField().primary_key
    activity_type = models.CharField(max_length = 255)
    activity_page_url = models.URLField()
    description = models.TextField(max_length = 255, blank = True)
    
    
class History(models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE).primary_key
    activity = models.ForeignKey('User_Activities', on_delete = models.CASCADE).primary_key
    
    
class Store(models.Model):
    product_id = models.AutoField().primary_key
    price = models.FloatField()
    product_type = models.CharField(max_length = 255)
    action_start = models.DateTimeField()
    action_end = models.DateTimeField(blank = True)
    privileges = models.SmallIntegerField(blank = True)
    

class Purchases(models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE).primary_key
    product = models.ForeignKey('Store', on_delete = models.CASCADE).primary_key
    
    
class Achievements(models.Model):
    achieve_id = models.AutoField().primary_key
    achieve_type = models.CharField(max_length = 255)
    rarity = models.SmallIntegerField()
    image = models.ImageField()
    

class Achieve(models.Model):
    user = models.ForeignKey('User', on_delete = models.CASCADE).primary_key
    achieve = models.ForeignKey('Achievements', on_delete = models.CASCADE).primary_key
    receiving_date = models.DateTimeField()
    
    
class Children_Groups(models.Model):
    group_id = models.AutoField().primary_key
    next_lesson_date = models.DateTimeField()
    group_rating = models.IntegerField()
    teacher = models.ForeignKey('Teacher_Users', on_delete = models.CASCADE)
    
    
class EnrollmentInGroup(models.Model):
    group = models.ForeignKey('Children_Groups', on_delete = models.CASCADE).primary_key
    child = models.ForeignKey('Child_Users', on_delete = models.CASCADE).primary_key
    enter_date = models.DateTimeField()
    exit_date = models.DateTimeField(blank = True)
    
    
class Group_Remote_Lessons(models.Model):
    lesson_id = models.AutoField().primary_key
    lesson_content = models.TextField(blank = True)
    lesson_theme = models.CharField(max_length = 255)
    group = models.ForeignKey('Children_Groups', on_delete = models.CASCADE)
    teacher = models.ForeignKey('Teacher_Users', on_delete = models.CASCADE)
    
    
class Individual_Remote_Lessons(models.Model):
    lesson_id = models.AutoField().primary_key
    lesson_content = models.TextField(blank = True)
    lesson_theme = models.CharField(max_length = 255)
    child = models.ForeignKey('Child_Users', on_delete = models.CASCADE)
    teacher = models.ForeignKey('Teacher_Users', on_delete = models.CASCADE)
    
    
class Lesson_Additional_Materials(models.Model):
    material_id = models.AutoField().primary_key
    group_lesson = models.ForeignKey('Group_Remote_Lessons', on_delete = models.CASCADE)
    individual_lesson = models.ForeignKey('Individual_Remote_Lessons', on_delete = models.CASCADE)
    lesson = models.ForeignKey('Teacher_Created_Lessons', on_delete = models.CASCADE)
    
    
class Lesson_Images(models.Model):
    material = models.ForeignKey('Lesson_Additional_Materials', on_delete = models.CASCADE).primary_key
    image = models.ImageField()
    
    
class Teacher_Created_Lessons(models.Model):
    lesson_id = models.AutoField().primary_key
    lesson_type = models.CharField(max_length = 63, blank = True)
    difficulty = models.IntegerField(blank = True)
    description = models.CharField(max_length = 255, blank = True)
    content = models.TextField(blank = True)
    teacher = models.ForeignKey('Teacher_Users', on_delete = models.CASCADE)
    
    
class Game_Lessons(models.Model):
    lesson = models.ForeignKey('Teacher_Created_Lessons', on_delete = models.CASCADE).primary_key
    child = models.ForeignKey('Child_Users', on_delete = models.CASCADE).primary_key


class Completed_Lessons(models.Model):
    lesson = models.ForeignKey('Teacher_Created_Lessons', on_delete = models.CASCADE).primary_key
    child = models.ForeignKey('Child_Users', on_delete = models.CASCADE).primary_key
    
    
class Lesson_Errors(models.Model):
    lesson = models.ForeignKey('Teacher_Created_Lessons', on_delete = models.CASCADE).primary_key
    child = models.ForeignKey('Child_Users', on_delete = models.CASCADE).primary_key
    
    
class Applications(models.Model):
    parent = models.ForeignKey('Parent_Users', on_delete = models.CASCADE).primary_key
    teacher = models.ForeignKey('Teacher_Users', on_delete = models.CASCADE).primary_key
