from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
import os
from .forms import ChatbotForm
import json 

# Set your OpenAI API key
def chatbot_query_view(request):
    genai.configure(api_key="AIzaSyCxleLvgJ5Oqn1hbl6-eUl6XUOFF_nPVbg")
    response = None
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )
    
    if request.method == 'POST':
        try:
            
            # Ensure the body contains JSON data
            user_input = json.loads(request.body).get('user_input')
            if not user_input:
                raise ValueError("No user input provided")
            prompt=""" 
            You are a helpful chatbot for a gaming tournament website. Assist users with questions about gaming tournaments, rules, joining competitions, schedules, prize pools, and other related topics. Respond with accurate and concise answers, under 3 sentences. Use clear and actionable language. If a query requires detailed information, provide a brief summary and suggest where they can find more details. Always be polite and professional in tone. Examples: 
            1. "How can I join a tournament?" → "To join, create an account, select a tournament from the 'Tournamnets' page, and click 'Register.' Follow the payment or confirmation steps if required."
            2. "What are the tournament rules for Call of Duty?" → "Standard Call of Duty rules apply: team size of 4, no cheating, and only approved maps allowed. Full rules are on the tournament page."
            3. "Where can I see my participations?" → "Go to your profile, click 'My participations,' and select the tournament to view your payment status and your participation."
            Keep responses direct and efficient to minimize token usage while maximizing helpfulness
            """
            # Generate response from the model
            chat_session = model.start_chat(
                history=[
                    {
                        "role": "model",
                        "parts": prompt,
                    },
                ]
            )
            response_text = chat_session.send_message(user_input)

            # Return the response as JSON
            return JsonResponse({'response': response_text.text}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    else:
        form = ChatbotForm()
        return render(request, 'chatbot/chatbot.html', {'form': form, 'response': response})
