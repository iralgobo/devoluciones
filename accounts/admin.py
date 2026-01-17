# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Campos adicionales", {"fields": ("tipo", "direccion")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Campos adicionales", {"fields": ("tipo", "direccion")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)