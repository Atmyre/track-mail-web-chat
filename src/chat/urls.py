from django.conf.urls import url, include
from . import views

app_name = 'chat'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', views.ChatView.as_view(), name='chats_num'),
    url(r'^$', views.ChatView.as_view(), name='chats'),
    url(r'^$', views.update_messages, name='post_message'),
    url(r'^get_messages/(?P<pk>[0-9]+)$', views.get_messages, name='get_messages')
]
