from django.conf.urls import url,include

from django.views.generic.base import RedirectView
import ckweibo.views

urlpatterns = [
    url(r'^weibohome/', ckweibo.views.home),
    url(r'^callback/', ckweibo.views.callback),
    url(r'^sendpage/commit/', ckweibo.views.commit),
    url(r'^sendpage/', ckweibo.views.sendpage),
    url(r'^.?',RedirectView.as_view(url='/ckweibo/weibohome/')),
]