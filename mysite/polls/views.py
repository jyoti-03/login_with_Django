from django.shortcuts import render, HttpResponse,redirect
# from polls.views import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    return render(request, 'login.html')
