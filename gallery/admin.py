from django.contrib import admin
from gallery.models import Gallery, Image
from cms.admin.placeholderadmin import PlaceholderAdmin

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_image',)
    search_fields = ['name']


admin.site.register(Gallery, PlaceholderAdmin)
admin.site.register(Image, ImageAdmin)