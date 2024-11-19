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
    tournament_instance = get_object_or_404(tournament, id=tournament_id)
    amount_in_cents = int(tournament_instance.price * 100)

    # Check if the user is already participating in the tournament, in the case of paying from participation list in profile
    participation_instance = participation.objects.filter(
        participant=request.user,
        tournament=tournament_instance
    ).first()

    #in the case of paying after registering for tournament and choosing name directly : the first time
    if not participation_instance:
        # Create a new participation instance if one does not exist
        participation_instance = participation.objects.create(
            participant=request.user,
            tournament=tournament_instance,
            team_name=request.POST.get('team_name')  # Ensure 'team_name' is sent from the form
        )

    if request.method == 'POST':
        intent = stripe.PaymentIntent.create(
            amount=amount_in_cents,
            currency='usd',
            metadata={'participation_id': participation_instance.id, 'tournament_id': tournament_instance.id}
        )

        # Check if a pending payment exists, or create a new one
        payment, created = Payment.objects.get_or_create(
            participation=participation_instance,
            defaults={
                'amount': tournament_instance.price,
                'stripe_payment_intent_id': intent['id'],
                'status': "pending"
            }
        )

        if not created:
            # Update intent ID if a pending payment already exists
            payment.stripe_payment_intent_id = intent['id']
            payment.save()

        return render(request, 'Payment/payment_form.html', {
            'participation': participation_instance,
            'tournament': tournament_instance,
            'stripe_public_key': settings.STRIPE_TEST_PUBLISHABLE_KEY,
            'client_secret': intent.client_secret
        })

    return render(request, 'Payment/payment_form.html', {
        'tournament': tournament_instance
    })
    



# Payment success

def payment_success(request, participation_id):
    # Fetch the participation instance
    participation_instance = get_object_or_404(participation, id=participation_id)
    
    # Retrieve the associated payment instance
    try:
        payment = Payment.objects.get(participation=participation_instance)
    except Payment.DoesNotExist:
        # Handle the case where the payment record does not exist
        return render(request, 'Payment/payment_error.html', {'message': 'Payment record not found'})

    # Check if the payment status is "pending" before updating it
    if payment.status == "pending":
        payment.status = "completed"
        payment.save()
        # Optionally, save or update the participation instance if needed
        participation_instance.save()
    else:
        # If the status is not "pending," display an appropriate message or handle it as needed
        return render(request, 'Payment/payment_error.html', {'message': 'Payment already completed or failed'})

    # Send the confirmation email
    send_confirmation_email(participation_instance)


    return render(request, 'Payment/payment_success.html', {'payment': payment})


# mailing feat
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_confirmation_email(participation_instance):
    
    subject = f'Payment Confirmation for Tournament {participation_instance.tournament.name}'
    to_email = participation_instance.participant.email

    # Render HTML email content using a template
    html_message = render_to_string('email/payment_confirmation.html', {'participation': participation_instance})
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        'bassembg.contact@gmail.com',  # The sender email
        [to_email],  # Recipient email
        html_message=html_message,  # HTML version of the email
    )