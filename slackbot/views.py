from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def gen_tests(request):
    spec = request.POST.get("text", "")

    return JsonResponse({
        "response_type": "in_channel",
        "text": f"✅ Django received your spec:\n{spec}"
    })