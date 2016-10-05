#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import loader, Context, RequestContext
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from weibo import APIClient

APP_KEY = '2144222432'
APP_SECRET = 'ac0a4758fed8a0472f5c4f5605e1d4bf'
CALLBACK_URL = 'http://127.0.0.1/ckweibo/callback/'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

def home(request):
    url = client.get_authorize_url()
    return render_to_response('weibohome.html',{'massage':url},RequestContext(request))

def callback(request):
    code = request.GET['code']
    r = client.request_access_token(code)
    access_token = r.access_token
    expires_in = r.expires_in
    client.set_access_token(access_token, expires_in)
    return HttpResponseRedirect('/ckweibo/sendpage/')

def sendpage(request):
    content = client.statuses.home_timeline.get()
    return render_to_response('sendpage.html',{"content":content},RequestContext(request))

@csrf_exempt
def commit(request):
    if request.method == 'POST':
        content = request.POST.get('body')
        client.statuses.update.post(status=content)
    return HttpResponseRedirect('/home/')