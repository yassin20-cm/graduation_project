from django.shortcuts import render
from .models import User
from .models import Request
# Create your views here.

def user_profile(request):

    return render(request,'control/user_profile.html',{'user':'yassin'})

def requests(request):

    return render(request, 'control/home.html', {'requests': Request.objects.all()})
