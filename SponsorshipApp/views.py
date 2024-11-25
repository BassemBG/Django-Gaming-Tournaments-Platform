from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from TournamentApp.models import tournament
from .forms import PreselectedSponsorshipForm, SelectableSponsorshipForm
from django.contrib import messages
 


# def sponsorship_form_view(request, tournament_id=None):
#     # If a specific tournament is preselected (user clicked "Sponsor")
#     if tournament_id:
#         tournament = get_object_or_404(Tournament, id=tournament_id)  # Ensure the tournament exists
#         if request.method == 'POST':
#             form = PreselectedSponsorshipForm(request.POST, initial={'tournament': tournament})
#             if form.is_valid():
#                 form.save()
#                 return redirect('sponsorship_form')  # Redirect on success
#         else:
#             form = PreselectedSponsorshipForm(initial={'tournament': tournament})
#         return render(request, 'coreApp/sponsorship_form.html', {'form': form, 'tournament': tournament})

#     # If no tournament is preselected, allow user to select from dropdown
#     else:
#         if request.method == 'POST':
#             form = SelectableSponsorshipForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('sponsorship_form')  # Redirect on success
#         else:
#             form = SelectableSponsorshipForm()
#         return render(request, 'coreApp/sponsors.html', {'form': form, 'tournaments': Tournament.objects.all()})


#this is the last functionnal version:
def sponsorship_form_view(request, tournament_id=None):
    print("Done 1")
    if tournament_id:
        tournament1 = get_object_or_404(tournament, id=tournament_id)
        print("Done 2")
        if request.method == 'POST':
            print("Done 3")
            form = PreselectedSponsorshipForm(request.POST, initial={'tournament': tournament})
            if form.is_valid():
                print("Done 4")
                sponsorship = form.save(commit=False)
                sponsorship.tournament = tournament1  # Ensure the tournament is saved
                sponsorship.save()
                messages.success(request, "Sponsorship successfully created!")
                # return redirect('sponsorship_list')
                return redirect('view_sponsorships', pk=request.user.pk)
            
        else:
            print("Done 5")
            form = PreselectedSponsorshipForm(initial={'tournament': tournament1})
        # return render(request, 'userApp/sponsorships.html', {'form': form, 'tournament': tournament})
        print("Done 6")
        return render(request, 'coreApp/sponsors.html', {'form': form, 'tournament': tournament1})

    else:
        print("Done 7")
        if request.method == 'POST':
            print("Done 8")
            form = SelectableSponsorshipForm(request.POST)
            print(form)
            if form.is_valid():
                print("Done 9")
                sponsorship = form.save(commit=False)
                sponsorship.sponsor = request.user  # Link the sponsorship to the logged-in user
                # form.save()
                sponsorship.save()
                messages.success(request, "Sponsorship successfully created!")
                # return redirect('sponsorship_list')
                return redirect('sponsorshipList', pk=request.user.cin)
                # return redirect('view_sponsorships')
                # return redirect('view_sponsorships', pk=request.user.pk)
            else:
                print("Form errors:", form.errors)
            
        else:
            print("Done 10")
            form = SelectableSponsorshipForm()
            print("Done 11")
        return render(request, 'userApp/sponsorships.html', {'form': form, 'tournaments': tournament.objects.all()})
        # return render(request, 'coreApp/sponsors.html', {'form': form})
    
    
    # else:
    #     if request.method == 'POST':
    #         form = SelectableSponsorshipForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             messages.success(request, "Sponsorship successfully created!")
    #             return redirect('sponsorship_list')
    #     else:
    #         form = SelectableSponsorshipForm()
    #     return render(request, 'coreApp/sponsors.html', {'form': form, 'tournaments': Tournament.objects.all()})  
    
    

    