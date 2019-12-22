from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html', {'key1':'value1'})

def count(request):
    return render(request, 'count.html')

