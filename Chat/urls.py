from django.urls import path
from chatterbot import ChatBot

from . import views

urlpatterns = [

 path('',views.home,name='home'),
 path('bot_search/', views.bot_search, name='bot_search')

]