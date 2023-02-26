from timeit import default_timer
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
def indexPage(request):
    context = {
        "time_running": default_timer(),

    }
    return render(request, 'EMSU_index/index.html', context=context)