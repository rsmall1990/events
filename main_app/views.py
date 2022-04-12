from urllib import response
from django.shortcuts import render
from django.http import HttpResponse


# Add the Cat class & list and view function below the imports
class Event:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, date, description, attendence):
    self.name = name
    self.date = date
    self.description = description
    self.attendence = attendence

events = [
  Event('Tie-die', '3.23.22', 'make a shirt!', 300),
  Event('Grocery Bingo', '4.1.22', 'skip the aisle!', 150),
  Event('Movie Night', '4.12.22', 'grab the popcorn!', 200)
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def events_index(request):
    return render(request, 'events/index.html', {'events': events})