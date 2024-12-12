from django.shortcuts import render
from django.http import JsonResponse
from transformers import pipeline
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
# Load intent classification model globally
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Predefined intents and descriptions
COMMANDS = {
    "home page": "home",
    "tournaments page": "Tournaments_View",
    # "profile page": "profile",
    "games page": "Games_list",
    "equipments page": "Equipments_View",
    "sponsor page": "Sponsors_form",
    "chatbot page": "chatbot_query",
}

def classify_command(text):
    """
    Use NLP model to classify the intent of the text.
    """
    labels = list(COMMANDS.keys())  # Keys as labels
    result = classifier(text, labels)
    best_match = result["labels"][0]  # Top matched label
    confidence = result["scores"][0]  # Confidence score for the match
    return best_match, confidence


@csrf_exempt
def process_voice_command(request):
    """
    Process the text input and classify the intent.
    """
    if request.method == "POST":
        data = request.body.decode("utf-8")
        data = json.loads(data)
        text = data.get("text", "").strip()

        # Classify the intent
        command, confidence = classify_command(text)
        description = COMMANDS.get(command, "Unknown command")

        return JsonResponse({
            "user_text": text,
            "command": command,
            "confidence": confidence,
            "description": description,
        })

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def redirect_based_on_command(request):
    """
    Handle redirection logic based on the command.
    """
    if request.method == "POST":
        data = request.body.decode("utf-8")
        data = json.loads(data)
        command = data.get("command", "").strip()

        if not command:
            return JsonResponse({"error": "No command provided"}, status=400)

        # Map the command to URLs
        url = None
        if command == "home page":
            url = reverse("home")
        elif command == "tournaments page":
            url = reverse("Tournaments_View")
        # elif command == "profile page":
        #     url = reverse("profile", kwargs={"pk": request.user.pk}) if request.user.is_authenticated else None
        elif command == "games page":
            url = reverse("Games_list")
        elif command == "equipments page":
            url = reverse("Equipments_View")
        elif command == "sponsor page":
            url = reverse("Sponsors_form")
        elif command == "chatbot page":
            url = reverse("chatbot_query")

        if url:
            return JsonResponse({"redirect_url": url})
        else:
            return JsonResponse({"error": f"Unrecognized command: {command}"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

def voice_debug_page(request):
    """
    Serve the voice.html template for testing the voice command functionality.
    """
    return render(request, "voiceapp/voice_debug.html")
