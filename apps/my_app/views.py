from __future__ import unicode_literals
from django.shortcuts import render, redirect 
import datetime, time
from models import Course


# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        'courses':courses
    }
    return render(request, 'my_app/index.html', context)

def courses(request):
    if request.method == 'POST':
       course_name = request.POST['course_name']
       course_description = request.POST['course_description']
       Course.objects.create(course_name = course_name, course_description = course_description)
    
    return redirect('/')


def confirm(request,id):
    
    context = {
        'course':Course.objects.get(id=id)
    }
    
    return render(request, 'my_app/confirm.html', context)

def destroy(request, id):
    course = Course.objects.get(id=id).delete()
    
    return redirect('/')



