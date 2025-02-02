from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # http://127.0.0.1:8000
    return HttpResponse("Welcome in our Hollymovie project.")


def hello(request):
    # http://127.0.0.1:8000/hello/
    # funkcionalita
    return HttpResponse("Hello, world!")


def hello2(request, word):
    # http://127.0.0.1:8000/hello2/cruel/
    return HttpResponse(f"Hello, {word} word!")


def hello3(request):
    # http://127.0.0.1:8000/hello3?word=cruel
    word = request.GET.get('word', '')
    return HttpResponse(f"Hello, {word} word!")


def hello4(request):
    # http://127.0.0.1:8000/hello4?word=word
    word = request.GET.get('word', '')
    context = {'word': word}
    return render(request=request,
                  template_name="hello.html",
                  context=context)


def add(request, num1, num2):
    return HttpResponse(f"{num1} + {num2} = {num1 + num2}")


def add2(request):
    # http://127.0.0.1:8000/add2 -> 0 + 0 = 0
    # http://127.0.0.1:8000/add2?num1=2 -> 2 + 0 = 2
    # http://127.0.0.1:8000/add2?num2=2 -> 0 + 2 = 2
    # http://127.0.0.1:8000/add2?num1=2&num2=3 -> 2 + 3 = 5
    # http://127.0.0.1:8000/add2?num2=2&num1=3 -> 3 + 2 = 5
    num1 = int(request.GET.get('num1', 0))
    num2 = int(request.GET.get('num2', 0))
    return HttpResponse(f"{num1} + {num2} = {num1 + num2}")


def add3(request):
    number1 = int(request.GET.get('num1', 0))
    number2 = int(request.GET.get('num2', 0))
    result_add = number1 + number2
    context = {'num1': number1,
               'num2': number2,
               'result': result_add}
    return render(request, "add.html", context)

