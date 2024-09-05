from django.shortcuts import render, HttpResponse

# Create your views here.
def indexpage(request):
    return render(request, 'index.html')

def loginpage(request):
    return render(request, 'login.html')

def registerpage(request):
    return render(request, 'register.html')

def aboutpage(request):
    return render(request, 'about.html')