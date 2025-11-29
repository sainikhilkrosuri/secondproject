from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
last_payload = {}

@csrf_exempt
def webhook(request):
    global last_payload
    if request.method == "POST":
        payload = json.loads(request.body)
        last_payload = payload
        print("Success")
        return JsonResponse({"status": "saved", "received": payload})
    return JsonResponse({"info": "Send a POST request successfully."})

def index(request):
    return render(request, "index.html", context={"a": last_payload})

