from django import forms
from.models import ProductsDisplay

class ProductInfo(forms.ModelForm):
    class Meta:
        model=ProductsDisplay
        fields='__all__'
        
