from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html', {'key1':'value1'})


def count(request):
    fulltext = request.GET['fulltext']

    wordlst = fulltext.split()
    wordcnt = len(wordlst)

    worddict = dict()
    for word in wordlst:
        worddict[word] = worddict.get(word, 0) + 1
    return render(request, 'count.html', {'fulltext': fulltext, 'wordcnt': wordcnt, 'worddict': worddict,
                                          'items': worddict.items()})

def about(request):

    return render(request, 'about.html')