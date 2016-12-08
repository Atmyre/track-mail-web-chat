from django.shortcuts import render
from django.views import generic
from .models import Event, EventSerializer
from rest_framework import viewsets
from django.db.models import Q


class EventsView(generic.ListView):
    model = Event
    template_name = 'event/events.html'
    context_object_name = 'latest_events_list'

    def dispatch(self, request, pk=None, *args, **kwargs):

        if not request.user.is_authenticated:
            return render(request, 'login/login.html', {'redirect_to': request.get_full_path})

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        events = super().get_queryset()

        events = Event.objects.filter(Q(user_to_show=self.request.user) | Q(author=self.request.user))
        return [event.get_descr() for event in events]

    def get_events(self):
        return [event.get_descr() for event in events]


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Create your views here.
