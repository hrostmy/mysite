from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main_page, name='main_page'),
    path('sign_in/', views.sign_in_view, name='sign_in'),
    path('register/', views.register, name='register'),
    path('profile/<str:username>', views.profile, name='profile'),
]
