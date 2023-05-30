from django import forms
from .models import Blog, Post, Category, Tag


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_name',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'content', 'slug', 'published', 'status')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
