from django.db import models

class BackgroundImage(models.Model):
    name = models.CharField(max_length=200)
    image_upload = models.ImageField(upload_to="image/backgrounds")
    is_published = models.BooleanField()
    
    
    def admin_image(self):
        if self.image_upload:
            return '<img src="/media/%s"/>' % self.image_upload
    
    admin_image.allow_tags = True
    
    def __unicode__(self):
    		return self.name