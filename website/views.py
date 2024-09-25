from django.shortcuts import render

# Create your views here.

def index(request):
    return render("<h1>Write to my boss</h1>")
