from django.shortcuts import render,redirect
from Comment.forms import Commentview
from Blogs.models import Post
# Create your views here.
from Comment.models import Comment
# Create your views here.
def showcomment(request,article_id):
	detailarticle=Post.objects.get(id=article_id)
	
	user=request.user
	if request.method == "POST":
		form=Commentview(request.POST,request.FILES)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.Commented_by=request.user.username
			comment.Article=detailarticle
			# Comment=form.cleaned_data['Comment']
			pk=detailarticle.pk
			print(pk)
			comment.save()
			return redirect('Comment:showcomment',article_id=detailarticle.pk)
	else:
		form = Commentview()
	showcomment=Comment.objects.filter(Article_id=detailarticle.id)
	return render(request,'Comment/showcomment.html',{'user':user,'form':form,'showcomment':showcomment,'detailarticle':detailarticle})

