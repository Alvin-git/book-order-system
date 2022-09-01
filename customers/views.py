from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'customers/dashboard.html')


def books(request):
    return HttpResponse('Books')


def user(request):
    return HttpResponse('user')

