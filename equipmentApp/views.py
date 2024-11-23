from django.shortcuts import render
from equipmentApp.models import Equipment
from django.http import HttpResponse  # For debugging response
from django.shortcuts import render
from equipmentApp.models import Equipment

def Equipments_View(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    if query:
        # Filter equipments based on description
        equipments = Equipment.objects.filter(description__icontains=query)
    else:
        # Retrieve all equipment if no search query is provided
        equipments = Equipment.objects.all()

    return render(request, 'coreApp/equipment.html', {'equipments': equipments, 'query': query})

def test_view(request):
    equipment = Equipment.objects.first()  # Retrieve the first equipment
    if equipment and equipment.eq_image:
        print(f"Image Name: {equipment.eq_image.name}")
        print(f"Image Path: {equipment.eq_image.path}")
        print(f"Image URL: {equipment.eq_image.url}")
    else:
        print("No Image or No Equipment Found")
    return HttpResponse("Check the server logs for the image details.")