#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    print('home')
    # return HttpResponse('home do app')

    context = {
        'text': 'Olá Home',
        'title': 'Home -',
    }

    return render(
        request,
        'home/home.html',
        #'global/base.html'
        context,
    )


