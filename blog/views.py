from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext, Context, loader

from blog.models import Post
from blog.forms import PostForm

def post(request):
    post_list = Post.objects.all().order_by('title')

    form = PostForm()
    context = {
     'form': form,
     'title': 'loren impsun bla bla bla',
     'post_list': post_list
    }

    return render_to_response('blog/template_blog.html',context,
        context_instance=RequestContext(request))



