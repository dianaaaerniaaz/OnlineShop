from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страница приложения Асcessory.")
def categories(request,catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Аксессуары по категориям.</h1><p>{catid}</p>")
def archive(request, year):
    if int(year)> 2022:
        #raise Http404()
        #return redirect('/', permanent = True)
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам.</h1><p>{year}</p>")
def  pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>404-Страница не найдена</h1>')

