from django.shortcuts import render
from TournamentApp.models import tournament

def Tournaments_View(request):
    tournaments = tournament.objects.all()
    return render(request, 'coreApp/    <!-- banner part start-->
        <section class="banner_part">
            <div class="container">
                <div class="row align-items-center justify-content-between">
                    <div class="col-lg-6 col-md-8">
                        <div class="banner_text">
                            <div class="banner_text_iner">
                                <h1>Best Highlights
                                    of the Latest</h1>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                                    sed do eiusmod tempor incididunt ut labore et dolore
                                    magna aliqua. Quis ipsum </p>
                                <a href="#" class="btn_1">Watch Tutorial</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- banner part start-->.html', {'tournaments': tournaments}) 
