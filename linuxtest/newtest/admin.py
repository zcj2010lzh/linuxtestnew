from django.contrib import admin
from .models import  *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['account','password']


admin.site.register (UserModel,UserAdmin)


class UserTokenAdmin(admin.ModelAdmin):
    list_display = ['user','token']


admin.site.register(UserTokenModel,UserTokenAdmin)