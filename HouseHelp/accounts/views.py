from django.shortcuts import render

# Create your views here.
def helper_register(request):
    return render(request, "register_as_helper.html")

def customer_register(request):
    return render(request, "register_as_customer.html")

def login(request):
    return render(request, "login.html")

