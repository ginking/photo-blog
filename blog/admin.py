from django.contrib import admin
from blog.models import BlogPost
from cms.admin.placeholderadmin import PlaceholderAdmin

admin.site.register(BlogPost, PlaceholderAdmin)