from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<int:pk>/', views.category_list, name="category_list")
    #path('item/<int:pk>/', views.item_detail, name='item_detail'),
]