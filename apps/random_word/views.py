from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):

    string = get_random_string(length=14)

    if 'counter' not in request.session:
        request.session['counter'] = 1
    request.session['counter'] += 1

    context = {
        "string": string,
        "counter": request.session['counter']
    }

    
    return render(request,'random_word/random_word.html', context)

def generate(request):
    return redirect('/random_word')

def reset(request):
    request.session['counter'] = 0
    return redirect('/random_word')
