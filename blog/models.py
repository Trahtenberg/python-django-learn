from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify # для привидения юрл к нужному виду
from time import time

def gen_slug(strg):
    # генерация строки слаг с добавлением даты
    new_slug = slugify(strg,allow_unicode=True)  # преведение строки в чпу
    return new_slug + '-' + str(int(time()))

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # переопределение метода сохраниения поста
        # генерация строки только при создании нового экземпляра в бд
        if not self.id: # если нет ай ди (только у объектов из оперативной памяти), когда объект создан но не сохранён в бд
            self.slug = gen_slug(self.title)
            super().save(*args, **kwargs)   # сохранение в родительской модели


    tags = models.ManyToManyField('Tag',blank=True, related_name='posts')
    # метод можно присваивать в любой модели с которой нужно связать
    # связывание моделей, задано название метода отношения в текущей модели
    # post_set название метода по умолчанию

    def get_absolute_url(self):
        #функция что бы не прописывать в шаблоне название маршрута и передавать в него путь из бд
        return reverse('post_detail_url',kwargs = {'slug':self.slug})
    def __str__(self):
        return self.title #так проще

class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)
    
    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs = {'slug':self.slug})