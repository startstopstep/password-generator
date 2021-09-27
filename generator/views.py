from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice


# Create your views here.

def home(request):
    return render(request, "generator/home.html", {"password": "ajsdjadja"})


def password(request):
    # Unicode table
    # https://ucarecdn.com/8a6ce363-1e0c-4593-8c1b-f22da0dda956/

    # characters_lower = list(map(chr, range(97, 123)))
    # characters_upper = list(map(chr, range(65, 91)))
    # numbers = list(map(chr, range(48, 58)))
    # special_symbols = list(map(chr, range(33, 48)))

    
    characters = list()
    length = int(request.GET.get("length", 12))
    generated_password = str()

    if request.GET.get("lowercase"):
        characters.append(list(map(chr, range(97, 123))))

    if request.GET.get("uppercase"):
        characters.append(list(map(chr, range(65, 91))))

    if request.GET.get("numbers"):
        characters.append(list(map(chr, range(48, 58))))

    if request.GET.get("special_symbols"):
        characters.append(list(map(chr, range(33, 48))))

    for i in range(length):
        generated_password += choice(characters[(randint(0, len(characters) - 1))])

    return render(request, "generator/password.html", {"password": generated_password})


def check(request):
    password = "example"

    return render(request, "generator/check.html")
