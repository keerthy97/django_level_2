from django.contrib import admin
from proapp2.models import User
# Register your models here.
# admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
admin.site.register(User,UserAdmin)

