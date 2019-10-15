from django.shortcuts import render
from .models import Films
from django.http import HttpResponse,JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def things(request):
    data = list(Films.objects.values())
    return JsonResponse({'data': data})