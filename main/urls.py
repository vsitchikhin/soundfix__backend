from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('signup/', signup, name='signip'),
    path('login/', login, name='login'),
]
