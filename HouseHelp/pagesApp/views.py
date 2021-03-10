from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")