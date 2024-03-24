from django.urls import path
from .views import home,room,checkview,send,getmessages

urlpatterns = [
    path('', home,name='home'),
    path('<str:room>/',room,name='room'),
    path('checkview',checkview,name='checkview'),
    path('send',send,name='send'),
    path('getMessages/<str:room>/',getmessages,name='getMessages')
]