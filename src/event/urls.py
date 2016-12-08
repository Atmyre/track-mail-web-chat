from django.conf.urls import url, include
from . import views

app_name = 'event'
urlpatterns = [
    url(r'last/$', views.EventsView.as_view(), name='events'),
]
