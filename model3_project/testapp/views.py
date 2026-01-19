from django.shortcuts import render
from testapp.models import employee

def emp(request):
    emp = employee.objects.all()
    return render(request, 'testapp/emp.html', {'emp': emp})




