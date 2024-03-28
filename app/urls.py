from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from project.settings import MEDIA_ROOT, MEDIA_URL 
urlpatterns = [
    path('', views.home,name='home'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('signup', views.signup,name='signup'),
    path('courses', views.courses,name='courses'),
    path('schedules', views.schedules,name='schedules'),
    path('report', views.report,name='report'),
    path('contactus', views.contactus,name='contactus'),
    path('blog', views.blog,name='blog'),
    path('news', views.news,name='news'),
    path('course/<str:slug>', views.coursePage , name='coursePage'),
    path('enroll/<str:slug>', views.enroll , name='enroll'),
    path('schedule/<str:slug>', views.schedule , name='schedule'),
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)