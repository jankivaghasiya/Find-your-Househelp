from django.urls import path
from . import views

app_name = "pagesApp"

urlpatterns = [
    path('contact/', views.contact, name = "contact"),
    path('', views.index, name = "index")
]
