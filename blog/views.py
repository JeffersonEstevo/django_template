#from django.http import HttpResponse
from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404

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

def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Http404('Post não existe.')        

    context = {
        'post': found_post,
        'title': found_post['title'] + ' - ',
    }
    
    return render(
        request,
        'blog/post.html',
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