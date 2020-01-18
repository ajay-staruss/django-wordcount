from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'index.html')
def count(request):
    fulltext = request.GET['FullText']
    wordlist = fulltext.split()

    worddict ={}
    sorteddict={}
    for i in wordlist:
        if i in worddict:
            worddict[i]+=1
        else:
            worddict[i]=1

    return render(request, 'count.html',{'fulltext': fulltext, 'count':len(wordlist),'worddict':worddict.items()})
def about(request):
    return render(request, 'about.html')
