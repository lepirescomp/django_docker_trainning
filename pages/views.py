from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page_view(self):
    return HttpResponse("Hello, world!")