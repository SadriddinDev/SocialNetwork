from django.contrib import admin
from post.models import Post, Comment, ViewPost


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'user', 'title', 'view_count']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'created_at', 'text']


@admin.register(ViewPost)
class ViewPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'post', 'user']
