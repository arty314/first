#from pdb import post_mortem
from django.db import models
#from django.conf import settings
from django.contrib.auth.models import User


class Blog(models.Model):
    # urls 호출
    blog_name = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_name

class Category(models.Model):
    name = models.CharField(max_length=100)

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body =  models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE) #null = True, blank=True 는 옵션. 없어도 괜찮다는 말임.

    def __str__(self):
        return self.comment
