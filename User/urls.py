from django.contrib import admin
from django.urls import path
from User import views
app_name = 'User'
urlpatterns = [
    path('base/',views.base,name='base'),
    path('signup/',views.signup,name='signup'),
    # path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('UserImage/<int:article_id>/',views.UserImage,name='UserImage'),
    # path('user/<int:article_id>/',views.user,name='user'),
]