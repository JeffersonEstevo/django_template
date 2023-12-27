#from django.http import HttpResponse
from django.shortcuts import render

def blog(request):
    print('blog')
    # return HttpResponse('blog do app')
    return render(
        request,
        'blog/blog.html'
   )

def exemplo(request):
    print('exemplo')
    # return HttpResponse('blog do app')
    return render(
        request,
        'blog/exemplo.html'
    )