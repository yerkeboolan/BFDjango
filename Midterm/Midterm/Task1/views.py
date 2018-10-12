from django.shortcuts import render
from .models import Restaurant

def restaurants(request):
    rests = Restaurant.objects.all()

    context = {
        'rests': rests
    }

    return render(request, 'base.html', context)
