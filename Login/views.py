from typing import ContextManager
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
import wolframalpha


# Create your views here.


def Login(request):
    return render(request,"chat.html")


def bot_search(request):
    query = request.GET.get('query')
    str=query

    
    try:
        if(str=='hi' or str=='Hi'):
                ans= "ChatBot:Hello"
            # return render(request, 'Index.html', {'ans': ans, 'query': query})
        elif(str=='hello' or str=="Hello"):
                  ans= "Bot:Hi..!"
            #return render(request, 'Index.html', {'ans': ans, 'query': query})
        elif(str=='how are you?' or str=='How Are You'):

                  ans="Bot:I'm Fine And You?"
            #return render(request, 'Index.html', {'ans': ans, 'query': query})
        elif(str=="'i'm fine to" or str=="'I'M Fine To"):

                   ans="Bot:Nice To Here That"
            #return render(request, 'Index.html', {'ans': ans, 'query': query})
        elif  str == "how are you" or "Hi there" or "How are you" or "Is anyone there?" or "Hey" or "Hola" or "Hello" or "Good day":

                 ans=  "Good to see you again"
         
        elif str == "Bye" or "See you later" or "Goodbye" or "Nice chatting to you, bye" or  "Till next time":
            ans= "Have a nice day"
        
        elif str == "Thanks" or  "Thank you" or "That's helpful" or "Awesome  thanks" or "Thanks for helping me":

                  ans= "Happy to help!"
        
        elif str=="what is your name":
            ans= "My Name Is ChatBot!"

        else:

           ans= "Bot:Sorry i dident get that"
        return render(request, 'chat.html', {'ans': ans, 'query': query})

            
    except Exception:
        try:
           if(str=='hi'):
                ans= "Bot:hello"
            # return render(request, 'Index.html', {'ans': ans, 'query': query})
           elif(str=='hello'):
                  ans= "Bot:hi"
            #return render(request, 'Index.html', {'ans': ans, 'query': query})
           elif(str=='how are you?'):

                  ans="Bot:i m fine and you?"
            #return render(request, 'Index.html', {'ans': ans, 'query': query})
           elif(str=="'i'm fine to"):

                   ans="Bot:nice to here that"
            #return render(request, 'Index.html', {'ans': ans, 'query': query})
           else:

                   ans= "Bot:Sorry i dident get that"
           return render(request, 'chat.html', {'ans': ans, 'query': query})


        except Exception:
                   ans = "FOUND NOTHING"
                   return render(request, 'chat.html', {'ans': ans, 'query': query})



        
     