
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .services.ai_service import generate_testcases


@csrf_exempt
def slack_generate_testcases(request):
    if request.method == "POST":
        feature_description = request.POST.get("text")

        if not feature_description:
            return JsonResponse({
                "response_type": "ephemeral",
                "text": "Please provide a feature description."
            })

        ai_output = generate_testcases(feature_description)

        return JsonResponse({
            "response_type": "in_channel",
            "text": ai_output
        })

    return JsonResponse({"text": "Invalid request method."})
