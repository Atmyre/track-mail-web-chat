from django import forms
from django.core.exceptions import ValidationError
from message.models import Message


class ChatForm(forms.Form):
    search = forms.CharField(required=False)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text', 'chat')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['chat'].widget = forms.HiddenInput()
