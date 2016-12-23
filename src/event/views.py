from django.shortcuts import render
from django.views import generic
from .models import Event, EventSerializer
from rest_framework import viewsets
from django.db.models import Q
from friends.models import Relation
from django.contrib.auth.models import User


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

        user_friends = User.objects.filter(
            Q(user_from_relations__user_to=self.request.user) | Q(user_to_relations__user_from=self.request.user))
        # user_friends = User.objects.all()
        events = Event.objects.filter(Q(user_to_show=self.request.user) | Q(user_to_show__in=user_friends))
        return events

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        if not self.request.user.is_authenticated:
            return context

        context['events_to_show'] = self.get_events()

        return context

    def get_events(self):
        user_friends = User.objects.filter(
            Q(user_from_relations__user_to=self.request.user) | Q(user_to_relations__user_from=self.request.user))
        events = Event.objects.filter(Q(user_to_show=self.request.user) | Q(user_to_show__in=user_friends))
        print([event.get_descr() for event in events])
        return [event.get_descr() for event in events]


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Create your views here.
