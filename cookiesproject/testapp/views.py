from urllib import response
from django.shortcuts import render
import datetime


# Create your views here.
def setcook(request):
    response = render(request, 'testapp/setcookies.html')
    response.set_cookie('fname', value='Nikhil', expires=datetime.datetime.now() + datetime.timedelta(days=1))
    return response

def getcook(request):
    responce = render(request, 'testapp/getcookies.html')
    name = request.COOKIES.get('fname')
    return render(request, 'testapp/getcookies.html', {'name': name})

def delcook(request):
    response = render(request, 'testapp/deletecookies.html')
    response.delete_cookie('fname')
    return response 
