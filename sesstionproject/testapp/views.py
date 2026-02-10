from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['first_name'] = 'Deva'
    return render(request, 'testapp/setsession.html')

def getsession(request):
    name = request.session.get('first_name')
    return render(request, 'testapp/getsession.html',{'name': name})

def delsession(request):
    if 'first_name' in request.session:
        del request.session['first_name']
    return render(request, 'testapp/delsession.html')