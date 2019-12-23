from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, parametro1, parametro2):
    parametro3 = parametro1 + parametro2
    return HttpResponse ('<h1>hello {} a soma do numero {} com o numero {} é = {}</h1>'.format(nome, parametro1, parametro2, parametro3))