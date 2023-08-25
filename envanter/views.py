from .models import Category, Component, Subcategory
from .forms import ComponentForm
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Component


def component_detail(request, component_id):
    component = get_object_or_404(Component, pk=component_id)
    return render(request, 'Popup2', {'component': component})

def parca_ekle(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = ComponentForm()
    return render(request, 'index.html', {'form': form})

#def Category

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

