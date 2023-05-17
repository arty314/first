from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    Blog_name = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.Blog_name

class Category(models.Model):
    name = models.CharField(max_length=100)

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 게시물 모델
class Post(models.Model): # pk값 지정 안 하면 Django가 알아서 판단하고 생성
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body =  models.TextField()
    image = models.ImageField(upload_to = 'post_images/')
    date = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, through='PostTag')


    def __str__(self):
        return self.title

# tag를 다대다 관계에 대한 연결 테이블로 설정.
class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #post에서도 다양한 tags를 추가함
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE) #tag를 보았을때, 연결된 다양한 post들이 보임

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE) #null = True, blank=True 는 옵션. 없어도 괜찮다는 말임.

    def __str__(self):
        return self.comment
