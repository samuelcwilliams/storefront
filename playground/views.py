from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# View functions take a request and provide a response.
# Could also be seen as request handlers.

def say_hello(request):
    return HttpResponse('initial view')