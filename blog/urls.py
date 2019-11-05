from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about/', views.aboutpage, name='about'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
