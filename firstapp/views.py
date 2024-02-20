from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def wish(request):
    message="<h1>Hi Buddy How are you</h1>"
    return HttpResponse(message)
