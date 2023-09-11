from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Финконтроль МВД</h1>")

def about(request):
    return HttpResponse("<h1>About us </h>")

# Create your views here.
