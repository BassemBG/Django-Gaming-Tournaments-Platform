from django.contrib.auth.views import LoginView, LogoutView,de
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import StreamingHttpResponse
import cv2
import face_recognition
import os

from .models import user as User
from TournamentApp.models import tournament
from Participation.models import participation
from SponsorshipApp.models import sponsorship
from .forms import CustomLoginForm

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

    return render(request, 'userApp/register.html', {'errors_dict': {}})


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


@login_required    
def profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    tournaments = tournament.objects.all()
    participations = participation.objects.filter(participant=user)
    return render(request, 'userApp/Profilee.html', {'user': user, 'tournaments': tournaments, 'participations': participations})


def view_participation(request, pk):
    user = get_object_or_404(User, pk=pk)
    participations = participation.objects.filter(participant=user)
    return render(request, 'userApp/Participation.html', {'user': user, 'participations': participations})


def view_sponsorships(request, pk):
    user = get_object_or_404(User, pk=pk)
    sponsorships = sponsorship.objects.all()
    participations = participation.objects.all()
    return render(request, 'userApp/sponsorships.html', {'user': user, 'participations': participations, 'sponsorships': sponsorships})


def update_user(request, pk):
    user = get_object_or_404(User, cin=pk)  # Get the user instance
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()  # Save the updated user information
        return render(request, 'userApp/UpdateProfile.html', {'user': user})  # Redirect to the user's profile or desired page
    return render(request, 'userApp/UpdateProfile.html', {'user': user})
