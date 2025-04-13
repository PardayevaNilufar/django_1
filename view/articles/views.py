from lib2to3.fixes.fix_input import context

from django.shortcuts import render,redirect
from .admin import Article
from .forms import ArticleForm,CategoriyaForm
from .models import Category


def addarticle(request):
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ArticleForm()
    context={
        "form":form
    }
    return render(request,"add_article.html",context)



def addcategoriya(request):
    if request.method=='POST':
        form=CategoriyaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=CategoriyaForm()
    context={
        "form":form
    }
    return render(request,"categoriya.html",context)




def detaile_page(request,id):
    categoriya=Category.objects.filter(id=id).first()
    context={
        "cate":cartigoriya
    }
    return render(request,"detaile.html",context)



















def delarticle(request,id):
    ochirish=Article.objects.get(id=id)
    if ochirish:
        ochirish.delete()
        return redirect('home')

def update_article(request,id):
    article=Article.objects.get(id=id)
    if request.method=='POST':
        form=ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ArticleForm(instance=article)
    context={
        "form":form
    }
    return render(request,"update_article.html",context)








def home_page(request):
    articles=Article.objects.all()
    categoriyas=Category.objects.all()
    context={
        "articles":articles,
        "categoriya":categoriyas
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

