from django.shortcuts import render
from .models import Category, Component
from django.shortcuts import render, redirect
from .forms import ComponentForm


def parca_ekle(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = ComponentForm()
    return render(request, 'index.html', {'form': form})

def Category

def index(request):
    search_model = request.GET.get('search_model')
    components = Component.objects.all()
    if search_model:
        components = components.filter(model__icontains=search_model)
    return render(request, 'inventory/index.html', {'components': components})

def index(request):
    categories = Category.objects.all()
    components = Component.objects.all()
    return render(request, 'index.htm', {'categories': categories, 'components': components})

