from django.urls import path
from chatterbot import ChatBot


from . import views

urlpatterns = [

 path('',views.Login,name='Login'),
 path('bot_search/', views.bot_search, name='bot_search')
]
