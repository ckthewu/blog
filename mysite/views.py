from django.http import HttpResponseRedirect

from django.shortcuts import render,render_to_response
from datetime import datetime
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout,get_user
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
def home(request):
    return render(request,'home.html',{'timenow':timezone.now(),'usernow':request.user})

@csrf_exempt
def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home/')
            #return render_to_response('login.html', {'error': True}, RequestContext(request))

def to_log_in(request):
    return render_to_response('login.html',{'error':False},RequestContext(request))

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/home/')