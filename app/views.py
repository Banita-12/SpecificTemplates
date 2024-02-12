from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from app.models import *

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    ordering=['sname']
    #template_name='app/school_list.html'
