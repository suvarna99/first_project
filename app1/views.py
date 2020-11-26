from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfunction(request):
    return HttpResponse('<h1>Hi this is my first code</h1>')


def myfunction2(request):
    return HttpResponse('<marquee>Hi this is my 2nd code</marquee>')

