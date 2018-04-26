from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index page")

def site(request):
    return HttpResponse("site page")
