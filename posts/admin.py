from django.contrib import admin
from .models import NewPost


@admin.register(NewPost)
class AdminPost(admin.ModelAdmin):
    list_display = ('user', 'caption',)
