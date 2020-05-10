from django import forms
from django.contrib import admin
#from ckeditor.widgets import CKEditorWidget

from Comment.models import Comment
class Commentview(forms.ModelForm):
    #description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Comment
        fields = ['Comment']