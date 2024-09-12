from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile


class CustomAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_superuser", "is_active","is_verified")
    list_filter = ("email", "is_superuser", "is_active","is_verified")
    searching_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        ("Authentictions",
            {
                "fields": ("email","password")
            },
        ),
        ("Permissions",
            {
                "fields": ("is_superuser","is_active","is_staff","is_verified")
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
admin.site.register(Profile)
