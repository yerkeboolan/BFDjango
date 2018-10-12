from django.shortcuts import render
from .models import Restaurant

def restaurants(request):
    res = Restaurant.objects.all()

    context = {
        'res': res
    }

    return render(request, 'base.html', context)
