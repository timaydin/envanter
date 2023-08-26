from django import forms
from .models import Component, Subcategory, Category

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['subcategory']

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = [
            'category', 
            'model', 
            'parca_no',
            'manufacturer', 
            'birim_fiyat', 
            'stock', 
            'ohm', 
            'w', 
            'technical_specifications', 
            'picture_url', 
            'document_url',
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
