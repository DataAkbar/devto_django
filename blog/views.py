from django.shortcuts import render
# from .models import Blog, Comment, Category
# from .forms import BlogForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required
# from django.db.models import Q
# from django.http import HttpResponse
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    # posts = Blog.objects.all()
    # cats = Category.objects.all()
    # paginator = Paginator(posts, 4)
    # page = request.GET.get('page')
    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html')  # , 'cats': cats}


# def detail(request, post_id):
#     post = Blog.objects.get(pk=post_id)
#     form = CommentForm(request.POST)
#
#     if form.is_valid():
#         new_comment = form.save(commit=False)
#         new_comment.author = request.user
#         new_comment.post = post
#         new_comment.save()
#     else:
#         form = CommentForm()
#
#     comments = Comment.objects.filter(post=post).order_by('-created_at')
#
#     return render(request, 'blog/detail.htm', context={'post': post, 'comments': comments, 'form': form})
#
#
# def category(request, slug):
#     data = Blog.objects.filter(category__slug=slug)
#     # cat = Category.objects.get(slug=slug)
#     # cats = Category.objects.all()
#     return render(request, 'blog/category.html', {'data': data})  # data, , 'cat': cat, 'cats': cats})
#
#
# @login_required(login_url="login")
# def add_post(request):
#     form = BlogForm
#     if request.method == "POST":
#         form = BlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = BlogForm()
#     return render(request, 'blog/addpost.html', context={'form': form})
#
#
# @login_required(login_url="login")
# def edit_post(request, post_id):
#     post = Blog.objects.get(pk=post_id)
#     form = BlogForm(instance=post)
#
#     if request.user != post.author:
#         return HttpResponse("Siz buni o'zgartira olmaysiz")
#
#     if request.method == "POST":
#         form = BlogForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#     return render(request, "blog/editpost.html", {"form": form})
#
#
# @login_required(login_url="login")
# def delete_post(request, post_id):
#     post = Blog.objects.get(pk=post_id)
#     if request.user != post.author:
#         return HttpResponse("Siz buni o'chira olmaysiz")
#     else:
#         post.delete()
#         return redirect('index')
#
#
# def search_post(request):
#     query = request.GET.get('query')
#     data = Blog.objects.filter(
#         Q(title__icontains=query) |
#         Q(text__icontains=query)
#     )
#     return render(request, 'blog/search.html', {'data': data})
#
#
def registerUser(request):
    # if request.user.is_authenticated:
    #     return redirect('index')
    # else:
    #     form = UserCreationForm()
    #     if request.method == "POST":
    #         form = UserCreationForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('login')

    return render(request, 'registration/signup.html')
#
#


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)

            if user is not None:
                login(request, user)
                return redirect('index')
    return render(request, 'registration/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
