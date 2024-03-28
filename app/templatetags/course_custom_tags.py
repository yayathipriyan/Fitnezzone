from atexit import register
from django import template
from app.mod.usercourse import UserCourse
register = template.Library()

@register.simple_tag
def is_enrolled(request , course):
    
    user = None
    if not request.user.is_authenticated:
        return False
    user = request.user
    try:
        course = UserCourse.objects.get(user = user, course=course)
        return True
    except:
        return False