from django.contrib import admin
from django.contrib.auth.models import User
from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('title','facilitator','venue','start_date','end_date',)
    search_fields =('title','facilitator',)


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title','author','published',)
    search_fields =('title','author',)

class CommunityAdmin(admin.ModelAdmin):
	list_display = ('community_name',)


admin.site.register(Event,EventAdmin)
admin.site.register(Blogs,BlogsAdmin)
admin.site.register(Community,CommunityAdmin)
admin.site.register(Project)
admin.site.register(User_community)
admin.site.register(ImageModel)




