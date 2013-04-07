from django.db import models
from cms.models.pagemodel import Page
from cms.models.fields import PlaceholderField
from gallery.models import Gallery

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    post_date = models.DateTimeField('date published')
    featured_image = models.ImageField(upload_to="images/blog/featured_images")    
    content_area = PlaceholderField('text', related_name="content_area")
    
    def __unicode__(self):
        return self.title