from django.contrib import admin

from ad.models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'post',
        'start_date',
        'end_date',
        'club',
    )
