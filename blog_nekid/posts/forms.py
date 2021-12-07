from django import forms
from django.forms import Textarea
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {
            'title': Textarea(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control'})
            }
