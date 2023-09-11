from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<h1>Финконтроль МВД</h1>")
#
# def about(request):
#     return HttpResponse("<h1>About us </h>")

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from Less_2_model_app.models import Author, Post


def hello(request):
    return HttpResponse("Hello World from function!")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


def year_post(request, year):
    text = ""
    ... # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):

        text = ""
        ... # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


def post_detail(request, year, month, slug):
     # Формируем статьи за год и месяц по идентификатору.
     # Пока обойдёмся без запросов к базе данных
    post = {
            "year": year,
            "month": month,
            "slug": slug,
            "title": "Кто быстрее создаёт списки в Python, list() или []",
            "content": "В процессе написания очередной программы задумался над тем, как"
                       "ой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {"name": "John"}
    return render(request, "less_3_tmpl/my_template.html", context)


class TemplIf(TemplateView):
    template_name = "less_3_tmpl/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
                'каждый': 'красный',
                'охотник': 'оранжевый',
                'желает': 'жёлтый',
                'знать': 'зелёный',
                'где': 'голубой',
                'сидит': 'синий',
                'фазан': 'фиолетовый',
        }

    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'less_3_tmpl/templ_for.html', context)


def index(request):
    return render(request, 'less_3_tmpl/index.html')


def about(request):
    return render(request, 'less_3_tmpl/about.html')


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'less_3_tmpl/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'less_3_tmpl/post_full.html', {'post': post})

# из домашнего задания

import form as form
from django.shortcuts import render
from .forms import ProductForm, ProductFormUpdate
from hw3.models import Product
import logging
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


def add_product(request):
    name = 'Добавление продукта'
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            # logger.info(f'Получили {name=}, {email=}, {age=}.')
            product = Product(name=name, description=description, price=price, quantity=quantity, image=image.name)
            product.save()
            message = 'product сохранён'
    else:
        form = ProductForm()
        message = 'Заполните форму'

    return render(request, 'hw4/product.html', {'form': form, 'message': message, 'name': name})


def update_product(request):
    name = 'Изменение продукта'
    if request.method == 'POST':
        form = ProductFormUpdate(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            product = form.cleaned_data['products']
            old_product = Product.objects.filter(pk=product.pk).first()
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            # logger.info(f'Получили {name=}, {email=}, {age=}.')
            # old_product(name=name, description=description, price=price, quantity=quantity, image=image.name)
            old_product.name = name
            old_product.description = description
            old_product.price = price
            old_product.quantity = quantity
            old_product.image = image.name
            old_product.save()
            message = 'product сохранён'
    else:
        form = ProductFormUpdate()
        message = 'Заполните форму'

    return render(request, 'hw4/product.html', {'form': form, 'message': message, 'name': name})


def index(request):
    return render(request, 'hw4/index.html')


def about(request):
    return render(request, 'hw4/about.html')