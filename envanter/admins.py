from django.contrib import admin
from .models import Category, Component, Subcategory, 
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('model', 'uretici', 'category', 'birim_fiyat', 'stok_miktar')

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory')