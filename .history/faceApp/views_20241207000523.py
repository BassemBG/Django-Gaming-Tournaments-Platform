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
def face_recognition_video(request):
    global match_status

    # Reset match status at the start of the view
    match_status = {"found": False, "name": None}

    droidcam_url = "http://192.168.1.2:4747/video"
    video_capture = cv2.VideoCapture(droidcam_url)

    frame_processing_interval = 5
    frame_counter = 0

    def generate():
        nonlocal frame_counter
        while True:
            ret, frame = video_capture.read()

            if not ret:
                print("Failed to grab frame")
                break

            if frame_counter % frame_processing_interval == 0:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                face_locations = face_recognition.face_locations(small_frame)
                face_encodings = face_recognition.face_encodings(small_frame, face_locations)

                for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]

                        match_status = {"found": True, "name": name}
                        print(f"Match found: {name}")

                        top, right, bottom, left = [int(x * 4) for x in (top, right, bottom, left)]
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                        cv2.putText(frame, f"Match found: {name}", (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 255, 0), 2)
                        break

                    top, right, bottom, left = [int(x * 4) for x in (top, right, bottom, left)]
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

            frame_counter += 1
            _, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')
