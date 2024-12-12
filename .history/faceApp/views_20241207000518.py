from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.http import StreamingHttpResponse
import cv2
import face_recognition
import os


# Path to the folder containing face images
known_faces_folder = os.path.join(os.getcwd(), "db")


# Initialize lists to store known face encodings and names
known_face_encodings = []
known_face_names = []

# Load and encode faces from the "db" folder
for filename in os.listdir(known_faces_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(known_faces_folder, filename)
        image = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(image)
        
        if face_encoding:
            known_face_encodings.append(face_encoding[0])
            known_face_names.append(filename.split('.')[0])

# View to stream the video feed for face recognition
from django.http import JsonResponse

# Global variable to track match status
match_status = {"found": False, "name": None}

def face_match_status(request):
    global match_status
    return JsonResponse(match_status)
