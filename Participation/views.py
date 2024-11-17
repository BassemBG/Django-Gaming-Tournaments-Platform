from django.shortcuts import render, redirect
from .models import participation  
from TournamentApp.models import tournament  
from userApp.models import user  as User
from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        cin = request.POST.get('user')
        tournament_id = request.POST.get('tournament')  # Get the tournament ID
        team_name = request.POST.get('team_name')

        # Retrieve the tournament instance
        Tournament = get_object_or_404(tournament, id=tournament_id)
        Userr = get_object_or_404(User, cin=cin)

        # Create a new participation instance
        new_participation = participation(
            participant=Userr,
            tournament=Tournament   ,  # Assign the tournament instance
            team_name=team_name
        )
        new_participation.full_clean()  # Validate the model
        new_participation.save()
        
        messages.success(request, 'Registration successful! You can now log in.')

        return redirect('participationList', pk=cin)
    return redirect('home')


from django.urls import reverse
from django.views.generic import DeleteView
from .models import participation  # Ensure you import your participation model

class ParticipationDeleteView(DeleteView):
    model = participation
    template_name = 'Participation/participation_confirm_delete.html'
    
    def get_success_url(self):
        # Get the instance of the participation being deleted
        participation_instance = self.object
        # Access the related participant (User) instance
        user = participation_instance.participant
        
        # Build the URL to redirect to the user's profile
        return reverse('participationList', kwargs={'pk': user.cin})  # Use 'pk' or the appropriate parameter name



# Payment Process

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
import stripe
from .models import participation, Payment
from TournamentApp.models import tournament

# Set Stripe secret key
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def process_payment(request, tournament_id):
    print("Form submitted for tournament:", tournament_id)
    tournament_instance = get_object_or_404(tournament, id=tournament_id)
    amount_in_cents = int(tournament_instance.price * 100)

    # Create a new participation instance
    participation_instance = participation.objects.create(
        participant=request.user,
        tournament=tournament_instance,
        team_name=request.POST.get('team_name')
    )

    if request.method == 'POST':
        intent = stripe.PaymentIntent.create(
            amount=amount_in_cents,
            currency='usd',  # Adjust the currency if needed
            metadata={'participation_id': participation_instance.id, 'tournament_id': tournament_instance.id}
        )

        # Save the payment info to the database (status = "pending")
        payment = Payment.objects.create(
            participation=participation_instance,
            amount=tournament_instance.price,
            stripe_payment_intent_id=intent['id'],
            status="pending"
        )

        return render(request, 'Payment/payment_form.html', {
            'participation': participation_instance,
            'tournament': tournament_instance,
            'stripe_public_key': settings.STRIPE_TEST_PUBLISHABLE_KEY,
            'client_secret': intent.client_secret  # Pass the client secret to the frontend
        })

    return render(request, 'Payment/payment_form.html', {
        'tournament': tournament_instance
    })




# Payment success

def payment_success(request, participation_id):
    # Fetch the participation instance
    participation_instance = get_object_or_404(participation, id=participation_id)
    
    # Assuming payment was successful, update the participation status and create a final record
    #participation_instance.status = "confirmed"  # or whatever you want to update
    participation_instance.save()

    # Optionally, save the payment success
    payment = Payment.objects.get(participation=participation_instance)
    payment.status = "completed"
    payment.save()

    return render(request, 'Payment/payment_success.html', {'payment': payment})

