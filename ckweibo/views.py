#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import loader, Context, RequestContext
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from weibo import APIClient
from mysite.settings import MyAPIClient as client,NUMPPAGE

def home(request):
    url = client.get_authorize_url()
    # return render_to_response('weibohome.html',{'massage':url},RequestContext(request))
    return HttpResponseRedirect(url)

def callback(request):
    AUTHCODE = request.GET['code']
    r = client.request_access_token(AUTHCODE)
    access_token = r.access_token
    expires_in = r.expires_in
    client.set_access_token(access_token, expires_in)
    return HttpResponseRedirect('/ckweibo/sendpage/')

def sendpage(request):
    if 'page' in request.GET:
        page = int(request.GET['page'])
    else:
        page = 1
    s = client.statuses.home_timeline.get(count=NUMPPAGE, page=page)
    contents = []
    i = 0
    while i <NUMPPAGE:
        si = s['statuses'][i]
        # if 'retweeted_status' in si.keys():
        #     contents.append('%s-----repost-----%s' % (si['text'],si['retweeted_status']['text']))
        # else:
        #     contents.append(si['text'])
        contents.append(si)
        i+=1
    # uid = client.account.get_uid.get()['uid']
    # user = client.users.show.get(uid=uid)['screen_name']
    user = ''
    context = {"contents":contents,'user':user,'page':page,'ppage':page-1,'npage':page+1}
    return render_to_response('sendpage.html',context,RequestContext(request))

@csrf_exempt
def commit(request):
    if request.method == 'POST':
        content = request.POST.get('body')
        client.statuses.update.post(status=content)
    return HttpResponseRedirect('/ckweibo/sendpage/')