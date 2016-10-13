from django.shortcuts import render

def login(request):
    return render(request, 'social_n/login.html')
