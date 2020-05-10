from django.contrib import admin
from django.urls import path
from Comment import views
app_name = 'Comment'
urlpatterns = [
	path('showcomment/<int:article_id>/',views.showcomment,name='showcomment'),
]