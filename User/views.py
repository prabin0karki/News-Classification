from django.shortcuts import render,redirect
# from User.forms import UserLoginForm
# from User.forms import UserSignup
from User.forms import UserRegisterForm,UserLoginForm,UserImageform
# Create your views here.
from Blogs.models import Post
from User.models import User
from django.contrib.auth import(authenticate,get_user_model,login,logout,)

def signup(request):
	if request.method == "POST":
		forms = UserRegisterForm(request.POST ,request.FILES)
		if forms.is_valid():
			user = forms.save(commit=False)
			username = forms.cleaned_data['username']
			password = forms.cleaned_data['password']
			user.set_password(password)
			user.save()
			#login
			new_user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('../login_user')
	else:
		forms=UserRegisterForm()
	return render(request, 'User/signup.html', {"forms": forms,})

def login_user(request):
	forms = UserLoginForm(request.POST or None)
	if forms.is_valid():
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('../../Blogs/index')
	return render(request, 'User/login.html', {"forms": forms,})



def base(request):
	sync_article=Post.objects.all()
	context = {'sync_article':sync_article}
	return render(request,'User/base.html',context)

def logout_user(request):
	logout(request)
	return redirect('../login_user')

def UserImage(request,article_id):
	Userid=User.objects.get(id=article_id)
	if request.method == "POST":
		forms = UserImageform(request.POST ,request.FILES,instance=Userid)
		if forms.is_valid():
			user = forms.save(commit=False)
			user.Username=Userid
			print(user.Username)
			pk=Userid.pk
			user.save()
			return redirect('Blogs:user_post')
	else:
		forms=UserImageform()
	return render(request, 'User/uploadeimage.html', {"forms": forms,})


# def user(request,article_id):
# 	user=request.user
# 	user_posts=Post.objects.filter(publish_by=request.user)
# 	showprofile=User.objects.filter(username=request.user)
# 	return render(request,'Blogs/userpost.html',{'user_posts':user_posts,'user':user,'showprofile':showprofile})