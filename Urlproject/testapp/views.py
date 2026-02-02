from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')

def emprec(request):
    return render(request,'testapp/emp.html',emprec,{'id:myid'})
