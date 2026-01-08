from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def testapp1_view(request):
    return HttpResponse("<h1>this is from Testapp1 view</h1>")


