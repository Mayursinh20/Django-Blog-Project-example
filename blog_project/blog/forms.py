from django import forms
from .models import Post

class PostNew(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'title'}))
    describe=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'desc'}))
    class Meta:
        model=Post
        fields=[
            'title',
            'author',
            'describe',
        ]
  

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=[
            'title',
            'describe',
        ]

