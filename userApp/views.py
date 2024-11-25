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


from SponsorshipApp.models import sponsorship
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


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
            # Display validation errors as messages
            for field, errors in e.message_dict.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")

    return render(request, 'userApp/register.html')

class CustomLoginView(LoginView):
    template_name = 'userApp/login.html'
    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('admin:index')
        else:   
            cin = self.request.user.pk
            if self.request.user.is_authenticated and cin:
                return reverse('profile', kwargs={'pk': cin})
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

    # Get the status filter from the query parameter
    status_filter = request.GET.get('status', None)

    # Filter sponsorships based on the user and the status filter
    # sponsorships = sponsorship.objects.filter(sponsor=user) 
    # Filter sponsorships by the logged-in user
    sponsorships = sponsorship.objects.all()
    if status_filter:
        sponsorships = sponsorships.filter(status=status_filter)

    # Pass the current filter to the template
    return render(request, 'userApp/sponsorships.html', {
        'user': user,
        'sponsorships': sponsorships,
        'status_filter': status_filter,
    })
    
def download_contract(request, id):
    try:
        # Fetch the sponsorship instance
        Sponsorship = sponsorship.objects.get(id=id)

        # Create a response object for the PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Sponsorship_info_{id}.pdf"'

        # Create a PDF canvas
        p = canvas.Canvas(response, pagesize=letter)
        p.setFont("Helvetica", 12)

        # Add content to the PDF
        p.drawString(100, 750, f"Sponsorship number {id} information")
        p.drawString(100, 730, f"Sponsor: {Sponsorship.sponsor}")
        p.drawString(100, 710, f"Tournament: {Sponsorship.tournament}")
        p.drawString(100, 690, f"Amount: {Sponsorship.amount}")
        p.drawString(100, 670, f"Start Date: {Sponsorship.start_date}")
        p.drawString(100, 650, f"End Date: {Sponsorship.end_date}")
        p.drawString(100, 630, f"Status: {Sponsorship.status}")

        # Add a footer
        p.drawString(100, 580, "Thank you for your sponsorship!")

        # Finalize the PDF
        p.showPage()
        p.save()

        return response
    except sponsorship.DoesNotExist:
        return HttpResponse("Sponsorship not found", status=404)

