from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/<int:id>/', views.user_profile, name='user_profile'),
    path('profile/<int:id>/<int:post_id>', views.post, name='post'),
    path('profile/<int:id>/<int:post_id>/user_tag', views.user_tags, name='user_tags'),
    path('profile/<int:id>/<int:post_id>/like', views.like, name='like'),
    path('profile/<int:id>/<int:post_user_id>/user', views.post_user_profile, name='post_user_profile'),
]