from django.shortcuts import render
from django.shortcuts import HttpResponse
import speech_recognition as sr
import pyttsx3
import wolframalpha
import wikipedia
import webbrowser
# Create your views here.


def home(request):
    return render(request,'Index.html')

def bot_search(request):
    query = request.GET.get('query')

    
    try:
        client = wolframalpha.Client("<--Your API key-->")
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'Index.html', {'ans': ans, 'query': query})

            
    except Exception:
        try:
            #ans = wikipedia.summary(query, sentences=10)
            ans = wikipedia.summary(query, sentences=100)
            return render(request, 'Index.html', {'ans': ans, 'query': query})


        except Exception:
            ans = "FOUND NOTHING"
            return render(request, 'Index.html', {'ans': ans, 'query': query})


