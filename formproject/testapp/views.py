from django.shortcuts import render
from testapp.forms import registrationForm
# Create your views here.
def showforms(request):
    reg=registrationForm()
    return render(request,'testapp/registration.html',{'regform:reg'})