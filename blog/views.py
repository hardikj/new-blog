from django.shortcuts import render_to_response
from blog.models import post

def home(request):
    post_list = post.objects.all().order_by('date')[:3]
    return render_to_response('home.html',{'post_list':post_list})

def show(request,post_id):
    try:
        p = post.objects.get(pk=post_id)
    except  post.DoesNotExist:
        raise Http404
    return render_to_response('show.html',{'post':p})

def archive(request):
    post_list = post.objects.all().order_by('date')
    return render_to_response('archive.html',{'post_list':post_list})

def about(request):
    p="hello"
    return render_to_response('about.html',{'p':p})
