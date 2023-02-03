from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.FeedListView.as_view(), name='index'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sign_in/', auth_views.LoginView.as_view(), name='sign_in'),
    path('register/', views.register, name='register'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('follow/<int:pk>', views.follow, name='follow'),
    path('<str:username>/', views.FeedListView.as_view(), name='user_feed'),
    path('<str:username>/followers', views.followers_and_followed, name='followers'),
    path('<str:username>/followed', views.followers_and_followed, name='followed'),
]