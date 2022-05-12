from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound  # , Http404
from django.views.decorators.csrf import csrf_exempt


def index(request):
    if request.GET:
        print(request.GET)
    return render(request, 'main/index.html')


@csrf_exempt
def lessons(request, lessonid):
    # if request.POST:
    #     print(request.POST)
    return HttpResponse(f'<h1>Страница уроков №{lessonid}</h1>')


@csrf_exempt
def singup(request):
    if request.POST:
        return HttpResponse('<h1>Страница регистрации POST</h1>')
    else:
        return HttpResponse('<h1>Страница регистрации</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
