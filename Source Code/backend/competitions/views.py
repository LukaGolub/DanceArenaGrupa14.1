from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    return HttpResponse('Hello World')

def live(req):
    return HttpResponse('LIVE')