from django.db import models
from cms.models.pagemodel import Page
from cms.models.fields import PlaceholderField


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="Unique url for gallery. Ex: Tree planting --> tree-planting")
    description = PlaceholderField('text', related_name="Gallery_description")
    icon = models.ImageField(upload_to="images/icons")
        
    def __unicode__(self):
        return self.name
        
class Image(models.Model):
    name = models.CharField(max_length=200)
    gallery = models.ForeignKey(Gallery)
    upload_image = models.ImageField(upload_to="images/featured", 
    													blank=True, 
    													null=True)

    def admin_image(self):
        if self.upload_image:
            return '<img src="/media/%s"/>' % self.upload_image
    
    admin_image.allow_tags = True
    
    def __unicode__(self):
        return self.name