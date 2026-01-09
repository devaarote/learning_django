from django.shortcuts import render,HttpResponse

# Create your views here.
def index(req):
    return HttpResponse("This is homepage of Hello world project")

def about(request):
    return HttpResponse("This is About page of Hello world project")

def services(request):
    return HttpResponse("This is Services page of Hello world project")