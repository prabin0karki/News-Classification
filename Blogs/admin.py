from django.contrib import admin

# Register your models here.
from Blogs.models import Post
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('Article_title','Category','id','Article_Short_Descriptions', 'Article_Content','publish_by','publish_date')
admin.site.register(Post,AuthorAdmin)