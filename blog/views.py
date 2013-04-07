from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import BlogPost

def all_posts(request):
    posts = BlogPost.objects.all().order_by('-post_date')
    context = {'posts': posts}
    return render_to_response('blog_home.html', context, context_instance=RequestContext(request))