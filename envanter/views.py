from django.shortcuts import render
from .models import Category, Component
from django.shortcuts import render, redirect
from .forms import ComponentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from .models import Component
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'index.html')

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


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Kullanıcıyı otomatik olarak giriş yapmış olarak işaretle
            login(request, user)
            return redirect('profile')  # Kayıt olduktan sonra profil sayfasına yönlendir
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
