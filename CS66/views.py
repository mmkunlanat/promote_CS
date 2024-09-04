from django.shortcuts import render, HttpResponse

# Create your views here.
def indexpage(request):
    return render(request, 'index.html')

def registerpage(request):
    return render(request, 'register.html')