#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    print('home')
    # return HttpResponse('home do app')
    return render(
        request,
        'home/home.html'
        #'global/base.html'
    )


