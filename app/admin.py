from django.contrib import admin
from .models import Schedule
from .models import Course, Tag , Prerequisite , Learning , Video
from app.mod import usercourse,userschedule
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag

class VideoAdmin(admin.TabularInline):
    model = Video

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin , LearningAdmin , PrerequisiteAdmin , VideoAdmin]    

admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(Schedule)
admin.site.register(usercourse.UserCourse)
admin.site.register(userschedule.UserSchedule)