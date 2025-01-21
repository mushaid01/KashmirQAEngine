import json
from django.shortcuts import render
from django.http import JsonResponse
from .agent import run_pipeline  

def chat_view(request):
    return render(request, 'index.html')

def send_message_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        if not user_message:
            return JsonResponse({"bot_message": "Please provide a valid question."})

        bot_response = run_pipeline(user_message)

        return JsonResponse({"bot_message": bot_response})

    return JsonResponse({"error": "Invalid request method."}, status=400)
