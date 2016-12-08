from django.shortcuts import render
from .models import Chat, ChatSerializer, Membership
from django.shortcuts import get_object_or_404, resolve_url
from message.models import Message
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from . import permissions
from django.db.models import Q
import json
from django.conf import settings
from django.utils.safestring import mark_safe
import requests
from django.views import generic
from .forms import ChatForm, MessageForm
from rest_framework.views import APIView
from urllib.error import HTTPError
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse


class ChatView(generic.CreateView):
    template_name = 'chat/chat.html'
    model = Message
    fields = ('text',)

    def dispatch(self, request, pk=None, *args, **kwargs):

        if not request.user.is_authenticated:
            return render(request, 'login/login.html', {'redirect_to': request.get_full_path})

        self.chat = None

        self.chat_id=pk

        if self.chat_id is not None:
            membership = get_object_or_404(Membership.objects.all(), user_chat_id=self.chat_id, user=request.user)
            self.chat = get_object_or_404(Chat.objects.all(), pk=membership.chat.id)
            print(self.chat.id)

        self.chats = [mem.chat for mem in Membership.objects.filter(user=request.user)]

        self.form = ChatForm(request.GET)
        self.form.is_valid()

        self.search_field = self.form.cleaned_data.get('search')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        if not self.request.user.is_authenticated:
            return context

        context['chat'] = self.chat
        context['chats'] = self.chats
        context['chat_id'] = self.request.GET.get('chat_id', None)
        context['messages'] = Message.objects.filter(chat=self.chat)

        return context


def update_messages(request):
    form = MessageForm(request.POST)
    form.instance.author = request.user
    data = {"success": True}
    form.save()
    return JsonResponse(data)


def get_messages(request, pk):
    return Message.objects.filter(chat_id=pk)


class ChatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    template_name = 'chat/chat.html'
    permission_classes = [permissions.IsInChat]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(users=self.request.user)

        name = self.request.GET.get('name')
        if name:
            qs = qs.filter(name__icontains=name)

        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

