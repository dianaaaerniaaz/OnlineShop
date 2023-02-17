from django.http import HttpResponse, HttpResponseNotFound,HttpResponseForbidden, Http404, HttpResponseBadError, HttpResponseServerError
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страница приложения Асcessory.")
def categories(request,catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Аксессуары по категориямv.</h1><p>{catid}</p>")
def archive(request, year):
    if int(year)> 2022:
        #raise Http404()
        #return redirect('/', permanent = True)
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам.</h1><p>{year}</p>")
def  pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>404-Страница не найдена</h1>')
def  pageForbidden(request, exception):
    return HttpResponseForbidden('<h1>403-Страница запрещена</h1>')

def  pageBadError(request, exception):
    return HttpResponseBadError('<h1>400-Плохой запрос</h1>')


# if(request.GET):
#         print(request.GET)


