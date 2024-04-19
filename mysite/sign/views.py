from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'sign/home.html')

def translate(request):
    if request.method == 'POST':
        return render(request, 'sign/translation.html')
    else:
        return HttpResponse("not found")