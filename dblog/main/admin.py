from django.contrib import admin
from main.models import *
from main import settings
from django.utils.html import format_html

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','create_date', 'modify_date','url','comments' )
    list_display_links = ('title', )
    def url(self,obj):
        return format_html('<a href="/{a}/">/{a}/</a>&nbsp;',a=obj.slug)
    url.description = "URL"
    url.allow_tags = True
    def comments(self,obj):
        return format_html('<a href="/admin/main/comment/?blogpost__id__exact={}">Comments</a>&nbsp;',obj.id)
    comments.description = "Comments List"
    comments.allow_tags = True

admin.site.register(BlogPost,BlogPostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_filter = ('by', 'blogpost')
    list_display = ('id','blogpost', 'by', 'content', 'create_date', )
    list_display_links = ('id', )

admin.site.register(Comment,CommentAdmin)

admin.site.site_title = settings.site_name
