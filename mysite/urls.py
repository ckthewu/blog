"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from django.views.generic.base import RedirectView
from mysite import views
from django.contrib.auth.views import login,logout

admin.autodiscover()

urlpatterns = [
    url(r'^blog/', include('blog.urls'), name = 'blog'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/in/', views.log_in),
    url(r'^login/', views.to_log_in),
    url(r'^logout/', views.log_out, name='logout'),
    url(r'^home/',views.home),
    url(r'^.?',RedirectView.as_view(url='/home/')),
]

