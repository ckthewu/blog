from django.conf.urls import url,include
import blog.views

urlpatterns = [
    url(r'^$',blog.views.home),
    url(r'^archive/(?P<id>\d+)/$', blog.views.detail, name='detail'),
    url(r'^archive', blog.views.archive),
    url(r'^create', blog.views.create_blogpost),

]
