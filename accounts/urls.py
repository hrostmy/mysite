from django.urls import path

from . import views

urlpatterns = [
    path('', views.FeedListView.as_view(), name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('main/', views.main_page, name='main_page'),
    path('sign_in/', views.sign_in_view, name='sign_in'),
    path('register/', views.register, name='register'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('follow/<int:pk>', views.follow, name='follow'),
    path('<str:username>/', views.feed, name='user_feed'),
    path('<str:username>/followers', views.followers_and_followed, name='followers'),
    path('<str:username>/followed', views.followers_and_followed, name='followed'),
]
