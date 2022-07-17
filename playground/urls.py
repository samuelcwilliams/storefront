from django.urls import path
from . import views

# URL Configuration
# Every app has it's own URL configuration
urlpatterns = [
    path('hello/', views.say_hello)
]