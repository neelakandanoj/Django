from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def time(reqiest):
    time=datetime.datetime.now()
    result='<h1>Time is :'+str(time)+'</h1>'
    return HttpResponse(result)
