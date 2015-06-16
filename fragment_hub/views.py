from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
    return render_to_response('index.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        print(name)
        print(password)

    return render_to_response('user/login.html', RequestContext(request))

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']
        if password == password_confirm:
            User.objects.create_user(name, email, password)

    return render_to_response('user/signup.html', RequestContext(request))

def change_password(request):
    if request.method == 'GET':
        return render_to_response('user/change_password.html')