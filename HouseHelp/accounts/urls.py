from django.urls import path
from . import views

urlpatterns = [
    path('register/helper/', views.helper_register),
    path('register/customer/', views.customer_register),
    path('login/', views.login),
]
