from django.urls import path

import polls.views
from . import views

urlpatterns = [
    path('create/', views.create, name='post_create'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete')
]
