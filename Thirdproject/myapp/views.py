from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse("This is my first view in Django!")

def second_view(request):
    return HttpResponse("This is my second view in Django!")

def third_view(request):
    return HttpResponse("This is my third view in Django!")
