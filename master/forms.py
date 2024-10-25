from django import forms
from .models import NewsModel

class NewsForm(forms.Form):

    class Meta:
        model = NewsModel
        fields = ['author', 'title', 'images', 'article']

