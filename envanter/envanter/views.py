from django.shortcuts import render
from .models import Category, Component

def index(request):
    categories = Category.objects.all()
    components = Component.objects.all()
    return render(request, 'index.htm', {'categories': categories, 'components': components})
