from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def new(request):
    return HttpResponse('Showing \'new\' view page')
def show(request):
    return HttpResponse('Showing \'show\' page')