from django.shortcuts import render
from django.http.response import HttpResponse
from arfi.models import *

# Create your views here.
def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")
