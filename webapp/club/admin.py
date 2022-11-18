from django.contrib import admin
from club.models import Club, Division


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'division',
        'name',
        'intro',
        'curriculum',
        'signup_condition',
        'recruitment_period_start',
        'recruitment_period_end',
        'representative_number',
        'place',
        'members_count',
    )
    list_filter = (
        'name',
        'members_count',
        'recruitment_period_start',
        'recruitment_period_end',
    )


admin.site.register(Division)
