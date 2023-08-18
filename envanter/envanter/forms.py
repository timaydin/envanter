from django import forms
from .models import Component

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['category', 'model', 'manufacturer', 'stock', 'ohm', 'w', 'technical_specifications', 'picture_url', 'document_url']

