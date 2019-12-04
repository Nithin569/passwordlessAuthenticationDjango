from django.http import HttpResponseRedirect
from django.shortcuts import render

def authlogin(request):
    if request.GET.get('username') != None and request.GET.get('username') != "":
        username = request.GET.get('username')
        user = authuser.objects.get(username=username)
        
        #manually set the backend attribute
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'tqs/login.html', {})
