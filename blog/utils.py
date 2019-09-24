from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        # tag = Tag.objects.get(slug=slug)
        obj = get_object_or_404(self.model,slug=slug)
        return render(request, self.template, context={self.model.__name__.lower():obj})