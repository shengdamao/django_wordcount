from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html', {'key1':'value1'})


def count(request):
    fulltext = request.GET['fulltext']
    print("request_print:")
    print(request)

    wordlst = fulltext.split()
    wordcnt = len(wordlst)

    worddict = dict()
    for word in wordlst:
        worddict[word] = worddict.get(word, 0) + 1
    return render(request, 'count.html', {'fulltext': fulltext, 'wordcnt': wordcnt, 'worddict': worddict,
                                          'items': worddict.items()})

def about(request):
    return render(request, 'about.html')

def game_01(request):
    return render(request, 'game_01.html')

def game_02(request):
    return render(request, 'game_02.html')

def sign_up(request):
    return render(request, 'sign_up.html')