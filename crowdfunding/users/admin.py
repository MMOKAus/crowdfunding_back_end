from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from copy import deepcopy

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields to show in the user list
    list_display = ('email', 'username', 'is_staff', 'is_active')

    
    fieldsets = deepcopy(UserAdmin.fieldsets)
    add_fieldsets = deepcopy(UserAdmin.add_fieldsets)
# Register your models here.
