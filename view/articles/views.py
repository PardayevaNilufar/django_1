from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .admin import Article

def home_page(request):
    articles=Article.objects.all()
    context={
        "articles":articles
    }

    return render(request,"home.html",context)

def fan_page(request):
    return render(request,"fan.html")

def detail_page(request,id):
    article=Article.objects.filter(id=id).first()
    context={
        "articl":article
    }
    return render(request,"detail.html",context)

