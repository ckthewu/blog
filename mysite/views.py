from django.http import HttpResponseRedirect

from django.shortcuts import render,render_to_response
from datetime import datetime
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
def home(request):
    return render(request,'home.html',{'timenow':timezone.now(),'usernow':request.user})

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return HttpResponseRedirect('/home/')

def to_log_in(request):
    return render(request,'login.html')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/home/')