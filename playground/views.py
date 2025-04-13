from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def greeting_function(request):
    return HttpResponse("Hello!")

def about_function(request):
    return HttpResponse("This is a test project using Django")

def add_function(request,a,b):   #must be 'a' and 'b' because we defined like this on urls.py
    return HttpResponse(a+b)

def intro_function(request,name,age):
    my_dictionary = {
        "name" : name,
        "age" : age
    }
    return JsonResponse(my_dictionary)

def first_page(request):
    return render(request,'index.html')
