from django.contrib import admin
from .models import Category, Component, Subcategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('category', 
                    'model', 
                    'parca_no',
                    'manufacturer', 
                    'birim_fiyat', 
                    'stock', 
                    'location_type',
                    'ohm', 
                    'w', 
                    'technical_specifications', 
                    'picture_url', 
                    'document_url', 
                
                )

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory')
