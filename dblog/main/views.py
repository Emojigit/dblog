from django.shortcuts import render, redirect
from main.models import *
from main import settings
from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def post(request,slug: str):
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
            "description": b.description,
            "url": "http" + ("s" if META["SERVER_PORT"] == 443 else "") + "://" + META["SERVER_NAME"] + "/" + slug,
            "postid": b.id,
            "status": 200
        }
        if request.method == "POST":
            if isinstance(request.user,AnonymousUser):
                render_dict["commentmsg"] = "ERROR: Please log in before leaving comments."
                render_dict["status"] = 401
            else:
                if "content" not in request.POST:
                    render_dict["commentmsg"] = "ERROR: Missing comment content!"
                    render_dict["status"] = 400
                else:
                    render_dict["commentmsg"] = "Commented!"
                    replyto = request.POST["replyto"] if "replyto" in request.POST else "0"
                    replyto_apply = None
                    if replyto != "0":
                        try:
                            replyto = int(replyto)
                        except ValueError:
                            render_dict["commentmsg"] = "ERROR: Replyto invalid! (Invalid Integer)"
                            render_dict["status"] = 400
                        else:
                            if not Comment.objects.filter(id=replyto).exists():
                                render_dict["commentmsg"] = "ERROR: Replyto invalid! (Not Found)"
                                render_dict["status"] = 400
                            else:
                                replyto = Comment.objects.get(id=replyto)
                                if replyto.blogpost != b:
                                    render_dict["commentmsg"] = "ERROR: Replyto invalid! (BlogPost Invalid)"
                                    render_dict["status"] = 400
                                else:
                                    render_dict["commentmsg"] = "Commented with reply!"
                                    replyto_apply = replyto
                    c = Comment.objects.create(by=request.user,blogpost=b,content=request.POST["content"],replyto=replyto_apply)
                    c.save()

        render_dict["comments"] = Comment.objects.filter(blogpost=b)
        return render(request,"views.html",render_dict,status=render_dict["status"])
    else:
        render_dict = {
            "title": "404",
            "content": "<p>Page not found. <a href=\"/\">Go back to main page</a></p>",
            "sitename": settings.site_name,
        }
        return render(request,"views.html",render_dict,status=404)

def mainpage(request):
    META = request.META
    """
    content = ["<p>{}</p><div id=\"postlist\">".format(settings.welcome)]
    for x in BlogPost.objects.all():
        content.append("<div class=\"post\"><h2 class=\"posttitle\"><a href=\"/{slug}/\">{title}</a></h2><p class=\"postdescription\">{description}</p></div>".format(slug=x.slug,title=x.title,description=x.description if x.description != "" else x.content))
    content.append("</div>")
    content = ''.join(content)
    """
    render_dict = {
        "title": "Main Page",
        "welcome": settings.welcome,
        "sitename": settings.site_name,
        "og": True,
        "description": settings.welcome,
        "posts": BlogPost.objects.all(),
        "url": "http" + ("s" if META["SERVER_PORT"] == 443 else "") + "://" + META["SERVER_NAME"] + "/"
    }
    return render(request,"mainpage.html",render_dict)

def placeholder(request):
    return HttpResponse("PLACEHOLDER", status=500)

def login(request):
    META = request.META
    render_dict = {
        "title": "Login",
        "sitename": settings.site_name,
        "og": True,
        "description": "Login to " + settings.site_name,
        "url": "http" + ("s" if META["SERVER_PORT"] == 443 else "") + "://" + META["SERVER_NAME"] + "/login/",
    }
    return LoginView.as_view(template_name="login.html",extra_context=render_dict)(request)

def register(request):
    META = request.META
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        render_dict = {
            "title": "Register",
            "sitename": settings.site_name,
            "og": True,
            "description": "Register on " + settings.site_name,
            "url": "http" + ("s" if META["SERVER_PORT"] == 443 else "") + "://" + META["SERVER_NAME"] + "/register/",
            "form": UserCreationForm(),
        }
        return render(request,"register.html",render_dict)

def logout(request):
    META = request.META
    render_dict = {
        "title": "Logout",
        "sitename": settings.site_name,
    }
    return LogoutView.as_view(template_name="logout.html",extra_context=render_dict)(request)


