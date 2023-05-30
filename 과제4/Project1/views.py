from django.shortcuts import render
from .models import Blog, Post, Category, Tag
from .forms import BlogForm, PostForm, CategoryForm, TagForm

# from django.db import models
# from django.contrib.auth.models import User


def home(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-create_dt')
    categorys = Category.objects.filter().order_by('-create_dt')

    paginator = Paginator(posts, 5) # 객체, 끊어내는 개수
    pageNum = request.GET.get('page') # 끊은 객체들을 dict타입으로 저장했다가 pageNumber로써 값을 조회할 수 있게 함
    posts = paginator.get_page(pageNum)
    categorys = paginator.get_page(pageNum)

    return render(request, 'index.html', {'posts':posts, 'categorys':categorys})
    


# Blog CRUD
def blog_creat(request):
    if request.method == 'BLOG':
        form = BlogForm(request.BLOG)
        if form.is_valid():
            blog = form.save()
            blog.owner = request.user
            return HttpResponseRedirect(reverse('blog_detail', args=[blog.pk]))
    else:
        form = BlogForm()
        return HttpResponseRedirect(reverse('blog_create'))

def blog_list(request):
    blog = Blog.blogobjects.all()
    print(f" blog_list : {posts} ")
    return HttpResponse('Blog list.')

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    print(f"blog_detail : {blog} ")
    return HttpResponse('Blog detail.')

def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.Blog, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('Blog_detail', pk=post.pk)
        else:
            form = BlogForm(instance=blog)
        return HttpResponse('Blog update.')

def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    messages.success(request, "Blog deleted successfully.")
    return redirect('home')


# Post CRUD
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.blog
            post.save()
            return HttpResponseRedirect(reverse('post_detail', args=[post.pk]))
    else:
        form = PostForm()
        return HttpResponseRedirect(reverse('post_create'))

def post_list(request):
    posts = Post.postobjects.all()
    print(f" post_list : {posts} ")
    return HttpResponse('Post list.')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(f" post_detail : {post} ")
    return HttpResponse('Post detail.')

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.blog
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return HttpResponse('Post update.')

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, "Post deleted successfully.")
    return redirect('home')


# Category CRUD
def category_create(request):
    if request.method == 'CATEGORY':
        form = CategoryForm(request.CATEGORY)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return HttpResponseRedirect(reverse('category_detail', args=[category.pk]))
    else:
        form = CategoryForm()
        return HttpResponseRedirect(reverse('category_create'))

def category_list(request):
    categories = Category.categoryobjects.all()
    print(f" category_list : {categories} ")
    return HttpResponse('Category list.')

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    print(f" category_detail : {category} ")
    return HttpResponse('Category detail.')

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'CATEGORY':
        form = CategoryForm(request.CATEGORY, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return HttpResponse('Category update.')

def post_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, "Category deleted successfully.")
    return redirect('category_list')
