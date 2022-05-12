from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('lesson/<int:lessonid>/', lessons, name='lesson'),
    path('singup/', singup, name='singip'),
]
