
import requests
import threading
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .utils import generate_testcases



def process_ai(feature_description, response_url):
    ai_output = generate_testcases(feature_description)

    requests.post(response_url, json={
        "response_type": "in_channel", 
        "text": ai_output
    })


@csrf_exempt
def slack_generate_testcases(request):
    if request.method == "POST":

        feature_description = request.POST.get("text")
        response_url = request.POST.get("response_url")

        # Start background thread
        thread = threading.Thread(
            target=process_ai,
            args=(feature_description, response_url)
        )
        thread.start()

        # Immediate response
        return JsonResponse({
            "response_type": "ephemeral",
            "text": "Generating testcases... please wait ⏳"
        })

    return JsonResponse({"error": "Invalid request"})