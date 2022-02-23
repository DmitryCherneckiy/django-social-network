from django.contrib import admin
from .models import Post, Like


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('id', 'author', 'content', 'created')


@admin.register(Like)
class AdminLike(admin.ModelAdmin):
    list_display = ('user', 'post', 'like', 'timestamp')

