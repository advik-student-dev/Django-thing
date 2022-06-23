from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# View function takes a request and gives a response 
# A request handler

def calc():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calc()
    
    """
    --------------------
    Real World Scenarios
    --------------------
    """
    # Pull data from db
    # Transform data
    # Send emails
    
    # return HttpResponse("Hello World!")
    return render(request, 'hello.html', {'name': 'Advik'})