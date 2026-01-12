from django.shortcuts import render

import datetime


# Create your views here.

def result(request):

    date=datetime.datetime.today()
    enm="ram prasad"
    esl=50000

    my_dict={'dt':date,'ename':enm,'esal':esl}
    return render(request,'testapp/result.html', my_dict)

def student(request):
    date=datetime.datetime.today()
    snm="Devendra Arote"
    smarks=95
    
    return render(request,'testapp/student.html')