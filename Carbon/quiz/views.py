from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, mother fucker!!! You're an asshole.")
def hello_view(request):
    return render(request, 'hello.html', {
        'data': "Hello Django ",
    })