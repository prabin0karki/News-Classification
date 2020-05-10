from django import forms
from django.contrib import admin
#from ckeditor.widgets import CKEditorWidget

from Blogs.models import Post
from Comment.models import Comment
class PostAdminForm(forms.ModelForm):
    #description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ['Article_title','Article_Short_Descriptions','Article_Content']

class Commentview(forms.ModelForm):
    #description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Comment
        fields = ['Comment']

# class SearchForm(forms.ModelForm):
# 	search=forms.CharField(max_length=100)
# 	class Meta:
# 		model=Post
# 		search_field