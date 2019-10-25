from django.shortcuts import render
from .models import Films
from django.http import HttpResponse, JsonResponse
from .forms import FilmForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def createform(request):
    form = FilmForm(request.POST or None)

    print(request.POST.get('film_name', None))
    data = {
        'form': form
    }
    return render(request, 'createform.html', data)


def things(request):
    # data = list(Films.objects.values())
    # data = ["Dave", "John"]
    title = "hello"
    # return JsonResponse({'data': data})
    data = {"name": "John", "age": 30, "car": None}
    #return render(request, 'things.html', {'data': data})
    return JsonResponse({'data': data})
