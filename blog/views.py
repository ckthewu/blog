#-*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from blog.models import BlogPost
from django.template import loader, Context, RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template.context_processors import request
import os,time
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
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
    return render_to_response('archive2.html',{'posts':posts,'error':False}, RequestContext(request))

# REPLACE BY class BlogView
# def archivepage(request):
#     blog_list = BlogPost.objects.all()
#     paginator = Paginator(blog_list, 10) # Show 10 contacts per page
#
#     page = request.GET.get('page')
#     try:
#         blog_list_page = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         blog_list_page = paginator.page(1)
#     except EmptyPage:
#         return render(request, 'blog_archive_page.html', {'posts': None, 'error': False})
#
#     return render(request, 'blog_archive_page.html', {'posts': blog_list_page,'error':False})



class BlogView(ListView):
    model = BlogPost
    template_name = 'blog_archive_page.html'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['error'] = False
        return context
    def get_queryset(self):
        return BlogPost.objects.order_by('-timestamp')

def BlogSearch(request):
    if 's' in request.GET:
        s = request.GET['s']
        if s:
            posts = BlogPost.objects.filter(title__icontains = s).order_by('-timestamp')
            if len(posts)==0:
                return render_to_response('archive2.html',{'posts':posts,'error':True}, RequestContext(request))
            else:
                return render_to_response('archive2.html',{'posts':posts,'error':False}, RequestContext(request))
    return HttpResponseRedirect('/archive/')


@csrf_exempt
def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(title=request.POST.get('title'),
                 body=request.POST.get('body'),
                 timestamp=timezone.now(),).save()
    return HttpResponseRedirect('/blog/archive/')

@login_required(login_url='/login/')
def create(request):
    return render(request, 'blog_create.html')

# class BlogCreateView(CreateView):
#     template_name = 'blog_create.html'
#     model = BlogView
#     post_save_redirect = '/blog/archive/'
#     login_required = True
#     fields = ['title','body']
#     def get_context_data(self, **kwargs):
#         context = super(BlogCreateView, self).get_context_data(**kwargs)
#         context['object']
#         return context
# def detail(request, id):
#     try:
#         post = BlogPost.objects.get(id=str(id))
#     except BlogPost.DoesNotExist:
#         raise 'Http404'
#     return render(request, 'detail.html', {'post' : post})

class BlogDetailView(DetailView):
    template_name = 'blog_detail.html'
    model = BlogPost
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        return context


# def bloglist(request):
#     posts = BlogPost.objects.all().order_by('-timestamp')
#     dates = sorted(posts.dates('timestamp', 'day'),reverse=1)
#     return render_to_response('bloglist.html',{'posts':posts,'dates':dates},RequestContext(request))

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'
    paginate_by = 30
    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['dates'] = sorted(BlogPost.objects.all().dates('timestamp', 'day'),reverse=1)
        return context
    def get_queryset(self):
        return BlogPost.objects.order_by('-timestamp')

