from django.shortcuts import render
from django.conf import settings
from django.contrib import messages


def index(request):
   return render( request,  'landing.html', {'name': 'fouda'})



 




