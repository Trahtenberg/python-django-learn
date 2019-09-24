from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

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