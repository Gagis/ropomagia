from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hei maailma! Kohta lisätään kortteja kantaan!")

def add(request):
    return HttpResponse("Pyydetään lappua ScryFallista.")

def cards(request):
    return HttpResponse("Listataan kerätyt tiedot lapuista.")
