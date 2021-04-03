from django.shortcuts import render
from ..accounts.models import Customer
from django.contrib.auth.models import User

# Create your views here.
def helper_register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['']
        phone = request.POST['phone']
        password1 = request.POST['pass']
        password2 = request.POST['cpass']
        email = request.POST['email']
        user = User.objects.create()
        customer = Customer(user = user)
    return render(request, "register_as_helper.html")

def customer_register(request):
    return render(request, "register_as_customer.html")

def login(request):
    return render(request, "login.html")

