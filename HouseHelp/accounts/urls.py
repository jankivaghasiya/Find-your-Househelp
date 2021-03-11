from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('register/helper/', views.helper_register, name = "helper"),
    path('register/customer/', views.customer_register, name = "customer"),
    path('login/', views.login, name = "login"),
]
