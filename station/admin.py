from django.contrib import admin
from .models import StationModel
from user.models import CustomUser
from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "is_staff", "is_active",)
    list_filter = ("username", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff","is_active", "groups", "user_permissions","roles"
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(StationModel)