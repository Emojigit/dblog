from django.shortcuts import render
from main.models import *
from main import settings

# Create your views here.

def post_get(request,slug: str):
    META = request.META
    if BlogPost.objects.filter(slug=slug).exists():
        b = BlogPost.objects.get(slug=slug)
        render_dict = {
            "title": b.title,
            "content": b.content,
            "created_at": b.create_date,
            "modify_at": b.modify_date,
            "sitename": settings.site_name,
            "blogpage": True,
            "og": True,
            "summary": b.description,
            "url": "http" + ("s" if META["SERVER_PORT"] == 443 else "") + "://" + META["SERVER_NAME"] + "/" + slug
        }
        return render(request,"views.html",render_dict)
    else:
        render_dict = {
            "title": "404",
            "content": "<p>Page not found. <a href=\"/\">Go back to main page</a></p>",
            "sitename": settings.site_name,
        }
        return render(request,"views.html",render_dict,status=404)

def mainpage(request):
    META = request.META
    content = ["<p>{}</p><div id=\"postlist\">".format(settings.welcome)]
    for x in BlogPost.objects.all():
        content.append("<div class=\"post\"><h2 class=\"posttitle\"><a href=\"/{slug}/\">{title}</a></h2><p class=\"postdescription\">{description}</p></div>".format(slug=x.slug,title=x.title,description=x.description if x.description != "" else x.content))
    content.append("</div>")
    content = ''.join(content)
    render_dict = {
        "title": "Main Page",
        "content": content,
        "sitename": settings.site_name,
        "og": True,
        "summary": settings.welcome,
        "url": "http" + ("s" if META["SERVER_PORT"] == 443 else "") + "://" + META["SERVER_NAME"] + "/"
    }
    return render(request,"views.html",render_dict)

