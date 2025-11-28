from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    render(request, 'templates/index.html')