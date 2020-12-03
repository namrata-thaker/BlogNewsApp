from django.urls import include,path
from . import views
from .api import BlogApi, BlogCreateApi, BlogUpdateApi, BlogDeleteApi

urlpatterns =[
    path('signup/',views.signup_view,name='signup'),
    path('saveuser',views.save_user,name='signup'),
    path('login',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('homepage/',views.homepage,name='homepage'),
    path('homepage/Myblogs/',views.Bloglist.as_view(),name="myblogs"),
    path('api/blog',BlogApi.as_view()),
    path('api/blog/create',BlogCreateApi.as_view()),
    path('api/blog/<int:pk>',BlogUpdateApi.as_view()),
    path('api/blog/<int:pk>/delete',BlogDeleteApi.as_view()),
    path('homepage/CreateBlog',views.create_view, name='createblog'),
    path('homepage/SaveBlog',views.create_blog_view, name='saveblog'),
    path('homepage/Myblogs/delete',views.delete_view, name='delete'),
    path('',views.index,name='index'),
]
