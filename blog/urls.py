from django.conf.urls import url,include
from blog.views import BlogListView
from django.views.generic.base import RedirectView
import blog.views

urlpatterns = [
    url(r'^bloghome/',blog.views.BlogView.as_view()),
    url(r'^archive/(?P<pk>\d+)/$', blog.views.BlogDetailView.as_view(), name='detail'),
    url(r'^archive/', blog.views.BlogView.as_view(),name='archive'),
    url(r'^create/commit/', blog.views.create_blogpost,name='commit'),
    url(r'^create/', blog.views.create, name='create'),
    url(r'^bloglist/', blog.views.BlogListView.as_view(),name='bloglist'),
    url(r'^search', blog.views.BlogSearch),
    url(r'^.?',RedirectView.as_view(url='bloghome/')),
]
