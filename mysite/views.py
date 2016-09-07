from django.shortcuts import render,render_to_response
from datetime import datetime
from django.utils import timezone
def home(request):

    return render(request,'home.html',{'timenow':timezone.now()})
