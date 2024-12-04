from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from myapp.models import Role

class UserModel(UserAdmin):
    pass

admin.site.register(Role, UserModel)

