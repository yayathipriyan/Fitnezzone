from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User

# Register your models here.
class Myauth(BaseBackend):
    def authenticate(email=None, password=None):
        
        try:
            user = User.objects.get(pk=email)
            #login_valid = (user.phone_number == int(phone_number))
            pwd_valid = check_password(password, user.password)
            if pwd_valid:
                return user
        except User.DoesNotExist:
            return None
        return None
    
    # def get_user(self, email):
    #     try:
    #         return User.objects.get(pk=email)
    #     except User.DoesNotExist:
    #         return None