import re
from main.models import *

# TODO: Enable Templates
"""
class TemplateRenderError(Exception):
    def __init__(self,tname,errmsg = "No error messages."):
        super().__init__()
        self.tname = tname
        self.errmsg = errmsg
    def __str__(self):
        return "Template {}: {}".format(self.tname,self.errmsg)

class TemplateNotFoundError(TemplateRenderError):
    def __init__(self,tname):
        super().__init__(tname,"Template nor found.")

class TemplateInvalidReturnError(TemplateRenderError):
    def __init__(self,tname,value):
        super().__init__(tname,"Template return value is invalid. ({})".format(value))

class TemplateCodeError(TemplateRenderError):
    def __init__(self,tname,ex):
        errmsg = "{}: {}".format(type(ex),ex.__str__())
        super().__init__(tname,errmsg)
        self.exception = ex



def render_template(tname,param):
    if Template.objects.filter(name=tname).exists():
        t = Template.objects.get(name=tname)
        code = t.pycode
        # [BUILDENV]
        env = {}
        env["re"] = re
        def GetBlogPage(slug):
            if BlogPost.objects.filter(slug=slug).exists():
                b = BlogPost.objects.get(slug=slug)
                return b.content
            else:
                return None
        env["GetBlogPage"] = GetBlogPage
        env["render_template"] = render_template # Don't worry, we have RecursionError
        loc = {"param": param}
        try:
            exec(code,env,loc)
        except Exception as e:
            raise TemplateCodeError(tname,e)
        if "r" not in loc or not isinstance(loc["r"], str):
            raise TemplateInvalidReturnError(tname, loc["r"] if "r" in loc else None)
        return loc["r"]
    else:
        raise TemplateNotFoundError(tname)


def render(pagename):
"""





