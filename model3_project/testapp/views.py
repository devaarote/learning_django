from django.shortcuts import render
from testapp.models import employee
from django.http import HttpResponse
from testapp.forms import EmployeeForm

# def emp(request):
#     emp = employee.objects.all()
#     return render(request, 'testapp/emp.html', {'emp': emp})


# def addemp(request):
#     en=4
#     enm="om"
#     esl=50000
#     emp=employee(eno=en,ename=enm,esal=esl)

#     emp.save()
#     return HttpResponse("<h1>Record insert succesfully<h1>")

# def updateemp(request,myid):
#     en=2
#     enm="Prathamesh Chaskar"
#     esl=100000
#     emp=employee(id=myid,eno=en,ename=enm,esal=esl)

#     emp.save()
#     return HttpResponse("<h1>Record update succesfully<h1>")

#     #update Employee set esal=esl whereid=2

# def delet(request,myid):

#     e = employee.objects.get(id=myid)
#     e.delete()
#     return HttpResponse("<h1> Record deleted succesfully")
    

def empinfo(request):
    emp=Employee.objects.all()   
    return render(request, 'testapp/emp.html', {'emp': emp}) 

def addemp(request):
    empfrm=EmployeeForm()
    return render(request,'testapp/addemp.html',{'empfrm:empfrom'})
