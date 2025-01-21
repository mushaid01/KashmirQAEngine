from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_view, name='chat_view'),
    path('chat/send_message', views.send_message_view, name='send_message'),
]
