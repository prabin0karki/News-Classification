from django.contrib import admin

# Register your models here.
from User.models import User
class UserAdmin(admin.ModelAdmin):
	list_display = ('username','id','first_name','last_name','email','bio','location','birth_date','Gender','Image')
admin.site.register(User,UserAdmin)

# class UserprofileAdmin(admin.ModelAdmin):
# 	list_display = ('Username','Username_id','Image')
# admin.site.register(Userprofile,UserprofileAdmin)