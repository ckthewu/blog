from django.conf.urls import url,include
from blog.views import BlogListView
from django.views.generic.base import RedirectView
import blog.views

urlpatterns = [
    url(r'^home',blog.views.home),
    url(r'^archive/(?P<pk>\d+)/$', blog.views.BlogDetailView.as_view(), name='detail'),
    url(r'^archive', blog.views.BlogView.as_view(),name='archive'),
    url(r'^create', blog.views.create_blogpost),
    url(r'^bloglist', blog.views.BlogListView.as_view(),name='bloglist'),
    url(r'^search', blog.views.BlogSearch),
    url(r'^.?',RedirectView.as_view(url='home'))
]
