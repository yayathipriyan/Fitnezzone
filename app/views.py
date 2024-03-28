from argparse import Action
from asyncio.windows_events import NULL
from email import message
from logging import error
from multiprocessing import context
from django.forms import ValidationError
from django.http import HttpResponse

from app.mod.userschedule import UserSchedule
#from .models import User, UserInfo
from .models import Course, Video, UserManager, Schedule
from app.mod.usercourse import UserCourse
from .auth import Myauth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#def index(request):
#    return HttpResponse("Hello, World!")

def home(request):
    return render(request, 'Home.html')
def login(request):
    return render(request, 'registration/login.html')
def signup(request):
    form=UserCreationForm
    if request.method=='POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'User has been registered')
            return redirect('login')
    return render(request, 'Signup.html',{'form':form})
def logout(request):
    Session.objects.all().delete()
    return redirect('/')
def courses(request):
    courses = Course.objects.all()
    print(courses)
    return render(request, 'Courses.html', context={"courses" : courses})
def schedules(request):
    schedules = Schedule.objects.all()
    print(schedules)
    return render(request, 'Schedule.html', context={"schedules" : schedules})
def report(request):
    global bmi
    if request.method=="POST":
        h=eval(request.POST.get('height'))
        w=eval(request.POST.get('weight'))
        hm=(h/100)
        bmi=(w/(hm*hm))
        if bmi>0 and bmi<=16:
            c="You've Severe Thinness"
        elif bmi>16 and bmi<=17:
            c="You've Moderate Thinness"
        elif bmi>17 and bmi<=18.5:
            c="You've Mild Thinness"
        elif bmi>18.5 and bmi<=25:
            c="You've Normal"
        elif bmi>25 and bmi<=30:
            c="You've Overweight"
        elif bmi>30 and bmi<=35:
            c="You've Obese Class I"
        elif bmi>35 and bmi<=40:
            c="You've Obese Class II"
        elif bmi>40:
            c="You've Obese Class III"
        
        context = {
            'bmi': bmi,
            'c' : c
        }
        return render(request, 'reports.html', context=context) 
    else: 
        return render(request, "reports.html")
def news(request):
    return render(request, 'Newsletter.html')
def contactus(request):
    return render(request,'contact_us.html')
def blog(request):
    return render(request,'blog.html')

def coursePage(request, slug):
    course=Course.objects.get(slug = slug)
    serial_number = request.GET.get("lecture")
    if serial_number is None:
        serial_number = 1 
    video = Video.objects.get(serial_number = serial_number, course = course)

    if(video.is_preview is False):
        if(request.user.is_authenticated is False):
            return redirect("login")
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user = user, course = course)
                error = "You have Already Enrolled in this Course"
            except:
                return redirect("courses")
    context = {
        "course" : course,
        "video" : video
    }
    return render(request, 'course_page.html', context=context)

@login_required(login_url='login')
def enroll(request , slug):
    course = Course.objects.get(slug = slug)
    user = request.user
    error = None 
    try:
        user_course = UserCourse.objects.get(user = user, course = course)
        error = "You have Already Enrolled in this Course"
    except:
        pass
    Price = None
    if error is None:
        Price = "Free"
    # if price is "Free" save enrollment object

    if Price=="Free":
        userCourse = UserCourse(user = user, course = course)
        userCourse.save()

    context = {
        "course" : course,
        "user" : user,
        "error" : error
    }
    
    return render(request,'regcourse.html', context=context)

@login_required(login_url='login')
def schedule(request , slug):
    name = Schedule.objects.get(slug = slug)
    user = request.user
    error = None 
    try:
        user_schedule = UserSchedule.objects.get(user = user, course = course)
        error = "You have Already Enrolled in this Course"
    except:
        pass
    Days = None
    if error is None:
        Days = "All Days"
    # if price is "Free" save enrollment object

    if Days == "All Days":
        userschedule = UserSchedule(user = user, name = name)
        userschedule.save()

    context = {
        "name" : name,
        "user" : user,
        "error" : error
    }
    
    return render(request,'regschedule.html', context=context)
