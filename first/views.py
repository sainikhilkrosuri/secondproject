from django.shortcuts import render
import json

# Create your views here.

def index(request):
    if request.methos == 'POST':
        req = json.loads(request.body)
    return render(request, 'index.html', context={'a':req})

