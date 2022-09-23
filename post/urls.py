from django.urls import path
import polls.views
from . import views


urlpatterns=[
    path('create/', views.create, name='post_create'),
    path('<int:pk>',polls.views.PostDetailView.as_view(), name='post_detail')
]