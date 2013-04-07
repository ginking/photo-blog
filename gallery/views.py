from django.shortcuts import render_to_response
from django.template import RequestContext
from gallery.models import Image, Gallery

def request_gallery(request, gallery_slug):
    project = Gallery.objects.get(slug=gallery_slug)
    pictures = Image.objects.filter(gallery=project)
    context = {'pictures': pictures}
    return render_to_response('gallery.html', context, context_instance=RequestContext(request))