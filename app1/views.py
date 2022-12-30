from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def str1(request):
    return HttpResponse('this is string one application')
    