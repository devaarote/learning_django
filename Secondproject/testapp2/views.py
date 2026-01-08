from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def testapp2_view(request):
    return HttpResponse("<h1>this is from Testapp2 view</h1>")