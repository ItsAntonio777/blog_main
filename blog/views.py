from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def detail(request, id):
    return render(request, 'detail.html', {'id': id})
