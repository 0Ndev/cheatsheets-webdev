from django.shortcuts import render
from .models import Cheatsheet


def index(req):
    return render(req, 'index.html')


def cheatsheets(req):
    cheatsheets = Cheatsheet.objects
    return render(req, 'cheatsheets.html', {'cheatsheets': cheatsheets})
