from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import get_object_or_404

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        # tag = Tag.objects.get(slug=slug)
        obj = get_object_or_404(self.model,slug=slug)
        return render(request, self.template, context={self.model.__name__.lower():obj})

class ObjectCreateMixin:
    
    form_model = None
    template = None

    # обработка запросов для создания тегов
    def get(self, request):
        # получить форму
        form = self.form_model()
        return render(request, self.template , context={'form':form})

    def post(self, request):
        # запрос на создание нового тега

        #slug = request.POST['title']

        #return HttpResponse(slug)

        bound_form = self.form_model(request.POST)  #можно передавать массивом, нужные значения сами заберуться

        if bound_form.is_valid():
            new_obj = bound_form.save()

            return redirect(new_obj) #редирект сразу по модели!
        return render(request,self.template,context={'form':bound_form})       