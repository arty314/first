from django.contrib import admin
from .models import Blog, Post, Comment, Category, Tag

# Register your models here.

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)