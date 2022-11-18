from django.contrib import admin
from review.models import Review


@admin.register(Review)
class ClubAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'post',
    )
