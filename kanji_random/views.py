from random import randint
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
def redirect(request):
    return HttpResponseRedirect('index/1')

def index(request,key):

    all_kanji = Kanji.objects.get(id=key)
    
    context = {
        'kanji': all_kanji
    }

    return render(request, 'kanji_random/index.html', context)

def random(request):
    count = len(Kanji.objects.all())
    random_kanji = randint(1, count)

    all_kanji = Kanji.objects.get(id=random_kanji)
    
    context = {
        'kanji': all_kanji
    }
    return render(request, 'kanji_random/index.html', context)
