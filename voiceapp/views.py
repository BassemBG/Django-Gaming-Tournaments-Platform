from django.shortcuts import render
from django.http import JsonResponse
from transformers import pipeline
import json
from django.views.decorators.csrf import csrf_exempt

# Load intent classification model globally
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Predefined intents and descriptions
COMMANDS = {
    "home": "Home page",
    "tournament": "Tournaments page",
    "profile": "Profile page",
    "Games": "Games page",
    "Equipments": "Equipments page",
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

def voice_debug_page(request):
    """
    Serve the voice.html template for testing the voice command functionality.
    """
    return render(request, "voiceapp/voice_debug.html")
