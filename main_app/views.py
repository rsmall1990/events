from .models import Event
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def events_index(request):
    events = Event.objects.filter(user = request.user)
    return render(request, 'events/index.html', {'events': events})

@login_required
def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', {'event': event})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - please try again'
    form = UserCreationForm()
    context = { 'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context)


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = '__all__'

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events/'