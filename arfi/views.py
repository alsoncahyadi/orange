from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import Context, loader
from arfi.models import *
import requests
import json

# Create your views here.
def index(request):
  r = requests.get("http://" + request.get_host() + '/api/clients')
  data = json.loads(r.text)
  return render(request, 'arfi/index.html', {'data': r})

def clients(request):
  r = requests.get("http://" + request.get_host() + '/api/clients')
  data = json.loads(r.text)
  return render(request, 'arfi/clients.html', {'data': r})
