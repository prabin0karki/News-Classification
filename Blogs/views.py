from django.shortcuts import render,redirect
from Blogs.forms import PostAdminForm
from Comment.forms import Commentview
import time
import datetime
# Create your views here.
from Blogs.models import Post
from Comment.models import Comment
from User.models import User
def add_post(request):
	user=request.user
	if request.method == "POST":
		form=PostAdminForm(request.POST,request.FILES)
		if form.is_valid():
			post_item = form.save(commit=False)
			post_item.publish_by=user.username
			post_item.save()
			return redirect('../../index')
	else:
		form = PostAdminForm()
	return render(request,'Blogs/post_form.html',{'form':form})


def index(request):
	showarticle=Post.objects.all().order_by('publish_date')
	context = {'showarticle':showarticle}
	return render(request,'Blogs/index.html',context)

def detail_article(request,article_id,format=None):

	detailarticle=Post.objects.get(id=article_id)
	showcomment=Comment.objects.filter(Article_id=detailarticle.id)
	form=Commentview(request.POST,request.FILES)
	if form.is_valid():
		post_item = form.save(commit=False)
		post_item.save()
		return redirect('../../../Comment/showcomment')
	else:
		form = Commentview()
	context = {'detailarticle':detailarticle,'form':form,'showcomment':showcomment}
	return render(request,'Blogs/detail_article.html',context)

def user_post(request):
	user=request.user
	user_posts=Post.objects.filter(publish_by=request.user)
	showprofile=User.objects.filter(username=request.user)
	return render(request,'Blogs/userpost.html',{'user_posts':user_posts,'user':user,'showprofile':showprofile})
