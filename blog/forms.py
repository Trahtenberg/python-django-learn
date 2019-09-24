from django import forms
from .models import Tag,Post
from django.core.exceptions import ValidationError

#класс отвечает за форму ввода и валидацию
class TagForm(forms.ModelForm):  #forms.Form без привязки к модели
    # title = forms.CharField(max_length = 50)
    # slug = forms.CharField(max_length = 50)

    # #переопределение классов у стандартных генераций формы
    # title.widget.attrs.update({'class':'my-class'})
    # slug.widget.attrs.update({'class':'my-class'})

    class Meta: # связывание формы и модели
        model = Tag
        fields = ['title','slug'] # поля которые будут в форме

        widgets = {
            'title': forms.TextInput(attrs={'class':'my-class','id':'titleTest'}), # добавление в конструктор атребутов
            'slug': forms.TextInput(attrs={'class':'my-class'}),
        }

    # своя валидация
    def clean_slug(self):   #клин метод костомный соглашение джанго_поле формы
        #автоматом в нижний регистр очищенные данные из формы
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('slug may not be "create"')
        if Tag.objects.filter(slug=new_slug).count():
            raise ValidationError('this name slug: {} already exist!'.format(new_slug))
        return new_slug

    # forms.ModelForm своя реализация 
    # def save(self): 
        
    #     new_tag = Tag.objects.create(title=self.cleaned_data['title'],slug=self.cleaned_data['slug'])
    #     return new_tag

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','slug','body','tags']

        widgets = {
            'title': forms.TextInput(attrs={'class':'title-class'}),
            'slug': forms.TextInput(attrs={'class':'slug-class'}),
            'body': forms.Textarea(attrs={'class':'textarea-class'}),
            'tags': forms.SelectMultiple(attrs={'class':'select-class'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('post not be "create"')
        return new_slug