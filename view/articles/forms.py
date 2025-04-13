from django import forms
from .models import Article,Category


class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=('title','description')
class CategoriyaForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=('name',)
