from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    context = {}
    if request.method == "POST":
        try:
            req = json.loads(request.body)
        except json.JSONDecodeError:
            req = {"error": "Invalid JSON"}
        context = {"a": req}
    return render(request, "index.html", context)

