#from django.http import HttpResponse
from django.shortcuts import render
from blog.data import posts

def blog(request):
    print('blog')
    # return HttpResponse('blog do app')

    context = {
        'text': 'Olá Blog',
        'title': 'Blog -',
        'posts': posts
    }
    
    return render(
        request,
        'blog/blog.html',
        context,
   )

def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Olá Exemplo',
        'title': 'Exemplo -',
    }

    # return HttpResponse('blog do app')
    return render(
        request,
        'blog/exemplo.html',
        context,
    )