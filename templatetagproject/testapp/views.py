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
    sname="Devendra Arote"
    sage=21
    sgrade="A+"

    my_dict={'dt':date,'sname':sname,'sage':sage,'sgrade':sgrade}
    return render(request,'testapp/student.html',my_dict)