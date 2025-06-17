from django.shortcuts import render
from .models import Tickets

# Create your views here.
def home(request):
    return render(request, "home.html")

def create(request):

    if request.method == "POST":
        # bila sumbit form
        print("Form submitted")
        print("From data", request.POST)

        # get data from request
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')

        user = request.user
        
        # try crete ticket
        Tickets.objects.create(title=title, description=description, user=user)

    else:
        # bila load form
        pass

    return render(request, "tickets/create.html")
