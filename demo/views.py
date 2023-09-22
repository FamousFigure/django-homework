import datetime
import os
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

egg = 8
milk = 0.4
salt = 2.0
cheese = 0.05
pasta_ = 0.3
cheese_for_buter = 1
bread = 1
tomato = 1
sausage = 1

def hello_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Available pages: '/', 'current_time/', 'work_dir/' ")

def current_time(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Time = {datetime.datetime.now().time()}')


def workdir(request: HttpRequest) -> HttpResponse:
    return HttpResponse()

def listdir(request):
    return HttpResponse(os.listdir())

def omlet(request):
    context_omlet = {
        'eggs': int(request.GET.get('servings', '1')) * egg,
        'milk': int(request.GET.get('servings', '1')) * milk,
        'salt': int(request.GET.get('servings', '1')) * salt}
    return render(request, 'omlet.html', context_omlet)

def pasta(request):
    context_pasta = {
        'cheese': int(request.GET.get('servings', '1')) * cheese,
        'pasta': int(request.GET.get('servings', '1')) * pasta_}
    return render(request, 'pasta.html', context_pasta)

def buter(request):
    context_buter = {
        'bread': int(request.GET.get('servings', '1')) * bread,
        'cheese_for_buter': int(request.GET.get('servings', '1')) * cheese_for_buter,
        'tomato': int(request.GET.get('servings', '1')) * tomato,
        'sausage': int(request.GET.get('servings', '1')) * sausage}
    return render(request, 'buter.html', context_buter)