from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
# Create your views here.
def index(req):
    return render(req,"index.hetml")