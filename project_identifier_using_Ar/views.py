from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
import datetime

from django.conf import settings
from django.contrib import messages




def home(request):
    context = {

    }

    return render(request, 'home/index.html', context)