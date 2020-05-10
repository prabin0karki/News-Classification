from django.db import models
import time
import datetime
# Create your models here.
from Blogs.models import Post
class Comment(models.Model):
	Comment=models.CharField(max_length=1000,blank=False,null=True)
	Commented_date = models.DateTimeField(editable=False)
	Commented_by=models.CharField(max_length=250,blank=False,null=True)
	Article=models.ForeignKey(Post,on_delete=models.CASCADE)
	def save(self):
		if not self.id:
			self.Commented_date = datetime.date.today()
		super(Comment, self).save()
