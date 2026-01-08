
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('f_view/',first_view),
    path('s_view/',second_view),
    path('t_view/',third_view),
    ]