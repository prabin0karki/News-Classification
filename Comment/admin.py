from django.contrib import admin

# Register your models here.
from Comment.models import Comment

class CommentAdmin(admin.ModelAdmin):
	list_display = ('Commented_by','Article_id','Article','Comment','Commented_date')
admin.site.register(Comment,CommentAdmin)
