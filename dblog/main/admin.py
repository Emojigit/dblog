from django.contrib import admin
from main.models import *
from main import settings

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','create_date', 'modify_date', )
    list_display_links = ('title', )

admin.site.register(BlogPost,BlogPostAdmin)

admin.site.site_title = settings.site_name
