from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'works.html')

def apiprojects(request):
    return render(request, 'api.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
