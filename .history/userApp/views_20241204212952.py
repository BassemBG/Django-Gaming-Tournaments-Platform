from django.contrib.auth.views import LoginView , LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect,reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import user as User
from django.views.generic import DetailView, UpdateView
from TournamentApp.models import tournament
from Participation.models import participation
from SponsorshipApp.models import sponsorship
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError

class UserDetailView(DetailView):
    model = User
    template_name = 'userApp/profile.html'
    context_object_name = 'user'
    ordering = ['username']


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        role = request.POST.get('role', 'Player')  # Default to 'Player' if not provided
        cin = request.POST['cin']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'userApp/register.html')
        errors_dict = {}
        try:
            new_user = User(
                username=username,
                cin=cin,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password),  # Hash the password before saving
                role=role,
                is_staff=True if role == 'admin' else False
            )

            new_user.full_clean()  # Run all model field validators
            new_user.save()  # Save to the database after validation passes

            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Replace with your actual success redirect URL

        except ValidationError as e:
            for field, errors in e.message_dict.items():
                errors_dict[field] = errors
                for error in errors:
                    messages.error(request, f"{field}: {error}")

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
        return render(request, 'userApp/register.html', {'errors_dict': errors_dict})    

    return render(request, 'userApp/register.html', {'errors_dict': errors_dict})

'''class CustomLoginView(LoginView):
    template_name = 'userApp/login.html'
    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('admin:index')
        else:   
            cin = self.request.user.pk
            if self.request.user.is_authenticated and cin:
                return reverse('profile', kwargs={'pk': cin})
            return reverse_lazy('home')
    '''
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    template_name = 'userApp/login.html'
    form_class = CustomLoginForm

    def get_form(self, form_class=None):
        """
        Override `get_form` to pass `request` to the form.
        """
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request.POST or None, request=self.request)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(self.get_success_url())
            else:
                return render(request, self.template_name, {'form': form, 'error': 'Invalid username or password.'})
        else:
            return render(request, self.template_name, {'form': form, 'error': 'Invalid captcha.'})

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('admin:index')
        else:
            cin = self.request.user.pk
            if self.request.user.is_authenticated and cin:
                return reverse_lazy('profile', kwargs={'pk': cin})
            return reverse_lazy('home')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    
def update_user(request, pk):
    user = get_object_or_404(User, cin=pk)  # Get the user instance
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()  # Save the updated user information
        return render(request,'userApp/UpdateProfile.html', {'user': user})  # Redirect to the user's profile or desired page
    return render( request,'userApp/UpdateProfile.html', {'user': user})


@login_required    
def profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    tournaments = tournament.objects.all()
    participations = participation.objects.filter(participant=user)
    return render(request, 'userApp/Profilee.html', {'user': user, 'tournaments': tournaments,'participations':participations})  # Pass games to the index template

def view_participation(request, pk):
    user = get_object_or_404(User, pk=pk)
    participations = participation.objects.filter(participant=user)
    return render(request, 'userApp/Participation.html', {'user': user,'participations':participations})

def view_sponsorships(request, pk):
    user = get_object_or_404(User, pk=pk)
    sponsorships = sponsorship.objects.all()
    participations = participation.objects.all()
    return render(request, 'userApp/sponsorships.html', {'user': user,'participations':participations,'sponsorships':sponsorships})



from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2
import face_recognition
import os

# Path to the folder containing face images
known_faces_folder = "db"

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
def face_recognition_video(request):
    # Initialize the camera feed from DroidCam
    droidcam_url = "http://192.168.0.178:4747/video"
    video_capture = cv2.VideoCapture(droidcam_url)
    
    frame_processing_interval = 5
    frame_counter = 0
    match_found = False  # Flag to track if a match has been found
    
    def generate():
        nonlocal frame_counter, match_found

        while True:
            ret, frame = video_capture.read()

            if not ret:
                print("Failed to grab frame")
                break

            if frame_counter % frame_processing_interval == 0:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Find all face locations and encodings in the current frame
                face_locations = face_recognition.face_locations(small_frame)
                face_encodings = face_recognition.face_encodings(small_frame, face_locations)

                for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]

                        # Display the name
                        cv2.putText(frame, f"Match found: {name}", (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 255, 0), 2)

                        match_found = True
                        break

                    top, right, bottom, left = [int(x * 4) for x in (top, right, bottom, left)]
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

            frame_counter += 1
            _, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

            if match_found:
                # Do the login logic here
                print(f"Match found: {name}")
                match_found = False
                break

    # Render the template with the video stream
    return render(request, 'face.html')

