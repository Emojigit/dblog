from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.

validate_even_re = re.compile("^[a-z0-9\-_]+$")

def slug_validate_even(value):
    if not bool(validate_even_re.match(value)):
        raise ValidationError("Slug can only contain [a-z0-9\-_].")

def name_validate_alnum(value):
    if not value.isalnum():
        raise ValidationError("Name must be alphanumberic.")

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50,validators=[slug_validate_even],unique=True)
    description = models.CharField(max_length=50,default="",blank=True)
    content = models.TextField()
    #render_template = BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True,editable=False)
    modify_date = models.DateTimeField(auto_now=True,editable=False)

# TODO: Enable Templates
"""
class Template(models.Model):
    name = models.TextField(max_length=50,validators=[name_validate_alnum],unique=True)
    pycode = models.CharField()
"""





