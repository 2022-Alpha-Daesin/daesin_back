from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Major, UserMajor

User = get_user_model()

admin.site.register(Major)
admin.site.register(UserMajor)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'nickname',
        'grade',
    )
