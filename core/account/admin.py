from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class CustomAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_superuser", "is_active")
    list_filter = ("email", "is_superuser", "is_active")
    searching_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        ("Authentications",
            {
                "fields": ("email","password")
            },
        ),
        ("Permissions",
            {
                "fields": ("is_superuser","is_active","is_staff")
            },
        ),
        ("Group Permissions",
            {
                "fields": ("groups","user_permissions")
            },
        ),
        ("Important Data",
            {
                "fields": ("last_login",)
            },
        ),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2"
            )}
        ),
    )
# Register your models here.
admin.site.register(User, CustomAdmin)