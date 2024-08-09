from django import forms

from app.models import Category, Subcategory


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name']
