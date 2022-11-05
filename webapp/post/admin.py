from django.contrib import admin
from post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'type',
    )
    list_filter = (
        'type',
    )
    ordering = (
        'created_at',
    )
