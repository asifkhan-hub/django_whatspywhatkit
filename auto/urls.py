from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_whatsapp_message, name='send_whatsapp_message'),
    path('message-sent/', views.message_sent, name='message_sent'),
]
