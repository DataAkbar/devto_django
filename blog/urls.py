from django.urls import path
from .views import (index, 
                    test, detail, add_post, 
                    category, edit_post, delete_post,
                    search_post, registerUser, loginUser,logoutUser)


urlpatterns = [
    path('', index, name="index"),
    path('test', test, name='test'),
    path('post/<int:post_id>/', detail, name="detail"),
    path('addpost/', add_post, name="addpost"),
    path('editpost/<int:post_id>/', edit_post, name="editpost"),
    path('deletepost/<int:post_id>/', delete_post, name="deletepost"),
    path('search/', search_post, name="search"),
    path('category/<str:slug>/', category, name="category"),
    path('signup/', registerUser, name="signup"),
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
]
