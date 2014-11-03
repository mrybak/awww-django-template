# coding=utf-8
import logging
from django.shortcuts import render

log = logging.getLogger('myapp.logger')

def index(request):
    log.debug("testowa wiadomosc")
    return render(request, 'zadanie/index.html')

