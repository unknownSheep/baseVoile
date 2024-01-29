from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.


def index(request):
    return HttpResponse("hello world")


def gear(request):
    context = {"latest_question_list": "boop"}
    return render(request, "gestion/listGear.html", context)


def adherents(request):
    return HttpResponse("adherents")

