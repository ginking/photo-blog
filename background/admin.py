from django.contrib import admin
from background.models import BackgroundImage

class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_image',)
    search_fields = ['name']


admin.site.register(BackgroundImage, BackgroundAdmin)
    
