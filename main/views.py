from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound  # , Http404
from django.views.decorators.csrf import csrf_exempt
from main.models import Users, User_Data, Teacher_Users
import json



def index(request):
    if request.GET:
        print(request.GET)
    return render(request, 'main/index.html')


@csrf_exempt
def signup(request):
    return HttpResponse('Hello')


@csrf_exempt
def login(request):
    return HttpResponse('<h1>Страница входа</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
