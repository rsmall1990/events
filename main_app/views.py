from .models import Event
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def events_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', {'event': event})

class EventCreate(CreateView):
    model = Event
    fields = '__all__'

class EventUpdate(UpdateView):
    model = Event
    fields = '__all__'

class EventDelete(DeleteView):
    model = Event
    success_url = '/events/'