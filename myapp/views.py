from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')  # Renderiza o template "index.html"

def about(request):
    return render(request, 'myapp/about.html')  # Renderiza o template "about.html"