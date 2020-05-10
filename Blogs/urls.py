from django.contrib import admin
from django.urls import path
from Blogs import views
app_name = 'Blogs'
urlpatterns = [
	path('index/<int:article_id>/',views.detail_article,name='detail_article'),
	path('add/post/',views.add_post,name='add_post'),
	path('index/',views.index,name='index'),
	path('user_post/',views.user_post,name='user_post'),
	]