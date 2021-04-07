from django.core.checks import messages
from django.shortcuts import render
from .models import Customer, Helper, Works
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def helper_register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        phone = request.POST['phone']
        dob = request.POST['dob']
        password1 = request.POST['pass']
        password2 = request.POST['cpass']
        email = request.POST['email']
        username = request.POST['username']
        user = User.objects.create(first_name=fname, last_name=lname, username=username, password=password1, email=email)
        works = Works()
        works.save()
        helper = Helper(user=user, address=address, contact_no=phone, dob=dob, works=works)
        helper.save()
        message = "User created"
        return render(request, "message.html", {'message':message})
    return render(request, "register_as_helper.html")

def customer_register(request):
    return render(request, "register_as_customer.html")

def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            message = "User is logged in"
        else :
            message = "Invalid username or password"
        return render(request, "message.html", {'message':message})
    return render(request, "login.html")

