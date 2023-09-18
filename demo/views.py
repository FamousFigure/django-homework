import datetime
import os
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.



def hello_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Available pages: '/', 'current_time/', 'work_dir/' ")

def current_time(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Time = {datetime.datetime.now().time()}')


def workdir(request: HttpRequest) -> HttpResponse:
    return HttpResponse()

def listdir(request):
    return HttpResponse(os.listdir())