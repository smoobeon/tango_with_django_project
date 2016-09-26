from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html',context=context_dict)

def about(request):
    my_age = 25
    my_address = 'Flurstrasse 36'
    context_dict = {'age': my_age, 'address': my_address}
    return render(request, 'rango/about.html', context=context_dict)