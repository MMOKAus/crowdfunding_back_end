from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     pass
#     model = CustomUser
# #     list_display = ('email', 'username', 'is_staff', 'is_active')  # show these in admin
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('full_name',)}),  # add extra fields here
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('full_name',)}),
    # )

# Register your models here.
