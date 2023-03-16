from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, Http404, HttpResponseServerError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

class ProductHome(ListView):
    model = Product
    template_name = 'accessory/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context


#def index(request):
#    posts = Product.objects.all()
    #cats = Category.objects.all()
#    context = {
#        'posts': posts,

#        'menu': menu,
#        'title': 'Главная страница',
#        'cat_selected': 0,
#    }

#    return render(request, 'accessory/index.html', context=context)
def about(request):
    return render(request, 'accessory/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'accessory/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context






# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


class ShowPost(DetailView):
    model = Product
    template_name = 'accessory/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>404-Страница не найдена</h1>')


def pageForbidden(request, exception):
    return HttpResponseForbidden('<h1>403-Страница запрещена</h1>')


def pageBadError(request, exception):
    return HttpResponse('<h1>400-Плохой запрос</h1>')

class ProductCategory(ListView):
    model = Product
    template_name = 'accessory/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context


# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#     }

# if(request.GET):
#         print(request.GET)

# if(request.GET):
#         print(request.GET)
