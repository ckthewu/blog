#-*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime,tzinfo
from blog.models import BlogPost
from django.template import loader, Context, RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template.context_processors import request
import os,time
# def index(request):
#     return HttpResponse(u"是不是是傻")
# Create your views here.

# def archive(request):
#     post = BlogPost(title = 'Title', body = 'Body', timestamp = datetime.now())
#     return render_to_response('archive.html', {'posts':[post]})

def home(request):
    return render(request, 'bloghome.html')

@csrf_exempt
def archive(request):
    posts = BlogPost.objects.all().order_by('-timestamp')[:10]
    return render_to_response('archive2.html',{'posts':posts,}, RequestContext(request))

@csrf_exempt
def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(title=request.POST.get('title'),
                 body=request.POST.get('body'),
                 timestamp=datetime.now(),).save()
    return HttpResponseRedirect('/blog/archive')
