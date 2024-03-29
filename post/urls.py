from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create, name='post_create'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/like', views.like_view, name='post_like'),
    path('<int:pk>/likes', views.likes, name='likes')
]
