from django import forms
from .models import Component, Subcategory, Category, Register



class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['subcategory']

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['category', 'model', 'manufacturer', 'stock', 'ohm', 'w', 'technical_specifications', 'picture_url', 'document_url']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'surname', 'email', 'phone', 'password']