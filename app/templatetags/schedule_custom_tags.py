from atexit import register
from django import template
from app.mod.userschedule import UserSchedule

register = template.Library()

@register.simple_tag
def is_scheduled(request , name):
    
    user = None
    if not request.user.is_authenticated:
        return False
    user = request.user
    try:
        name = UserSchedule.objects.get(user = user, name=name)
        return True
    except:
        return False