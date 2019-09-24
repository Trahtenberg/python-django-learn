from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import Post,Tag
#from django.shortcuts import get_object_or_404
from .utils import ObjectDetailMixin
from .forms import TagForm,PostForm


def posts_list(request):
    # return HttpResponse('<h3>Hello Roman! You top developer</h3>')

    #names = ['Sasha','Petya','Vova']

    posts = Post.objects.all()

    return render(request,'blog/index.html', context = {'posts': posts})

# def post_detail(request, slug):
#     post = Post.objects.get(slug=slug)   #slug_iexact не работает
#     return render(request, 'blog/post_detail.html', context={'post':post})

class PostDetail(ObjectDetailMixin,View):

    model = Post
    template = 'blog/post_detail.html'

    # оптимизация кода
    #def get(self, request, slug):
        #обрабатывает get запрос
        # post = Post.objects.get(slug=slug)   #slug_iexact не работает
        
        # post = get_object_or_404(Post,slug=slug)
        # return render(request, 'blog/post_detail.html', context={'post':post})

def tags_list(request):
    tags = Tag.objects.all()

    return render(request, 'blog/tags_list.html', context={'tags':tags})

# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag':tag})

class TagDetail(ObjectDetailMixin,View):
    model = Tag
    template = 'blog/tag_detail.html'

class TagCreate(View):
    # обработка запросов для создания тегов
    def get(self, request):
        # получить форму
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form':form})

    def post(self, request):
        # запрос на создание нового тега

        #slug = request.POST['title']

        #return HttpResponse(slug)

        bound_form = TagForm(request.POST)  #можно передавать массивом, нужные значения сами заберуться

        if bound_form.is_valid():
            new_tag = bound_form.save()

            return redirect(new_tag) #редирект сразу по модели!
        return render(request,'blog/tag_create.html',context={'form':bound_form})

class PostCreate(View): # создание/генерация вьюшки 

    def get(self,request):
        form = PostForm()
        return render(request, 'blog/post_create.html',context={'form':form})

    def post(self,request):
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request,'blog/post_create.html',context={'form':bound_form})


