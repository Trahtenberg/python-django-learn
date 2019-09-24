from django.urls import path
from .views import *    #импортировать файл с методами для отражения вью

urlpatterns = [
    path('', posts_list),
    path('post/create',PostCreate.as_view(),name='post_create_url'),
    path('post/<str:slug>/',PostDetail.as_view(), name='post_detail_url'),
    #метод во вью который будет это обрабатывать, str:slug обозначение юрл которое будет принимать функция во вью
    path('tag/create',TagCreate.as_view(),name='tag_create_url'),#должно быть выше, т.к. может возникнуть конфликт slug-ов
    path('tags/',tags_list, name = 'tags_list_url'),
    path('tag/<str:slug>',TagDetail.as_view(), name='tag_detail_url')
]