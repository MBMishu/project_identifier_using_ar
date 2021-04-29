from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
import datetime

from django.conf import settings
from django.contrib import messages

# Create your views here.
from home.model.models import *


# def home(request):
#     context = {

#     }

#     return render(request, 'home/index.html', context)


def showAr(request):

    product = Product.objects.all()
    context = {
        'product': product,
    }

    return render(request, 'home/main.html', context)
