from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')

def login(request):
    return render_to_response('user/login.html')

def signup(request):
    return render_to_response('user/signup.html')

def change_password(request):
    return render_to_response('user/change_password.html')