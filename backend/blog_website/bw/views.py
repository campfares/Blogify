from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    context = {
        'post': Post_data.objects.all(),
        'cat': Categories.objects.all(),
        'about_me' :About.objects.all(),
    }
    return render(request,'index.html',context)

def blog_page(request,pk):
    context={
        'post_id' : Post_data.objects.get(id = pk),
        'comment' : Comment.objects.filter(post_comment =  Post_data.objects.get(id = pk)),
        'all_post' : Post_data.objects.all(),
        'cat': Categories.objects.all(),
        'about_me' :About.objects.all(),
    }
    if request.method == "POST":
        name = request.POST['name']
        body = request.POST['body']
        new_comment = Comment(name=name ,post_comment =  Post_data.objects.get(id = pk) ,body=body)
        new_comment.save()
        return HttpResponse('<div>comment posted sucssefully<div/>')
    
    return render(request,'blocksignal.html',context)

def contact(request):
    context = {
        'post': Post_data.objects.all(),
        'cat': Categories.objects.all(),
        'about_me' :About.objects.all(),
    }
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        body = request.POST['body']

        contact_info = Contact(name=name,phone=phone,email=email,body=body)
        contact_info.save()
        return HttpResponse("<h1>i will responde soon<h1/>")

    return render(request,'contact.html',context)

def about(request):
    context = {
        'post': Post_data.objects.all(),
        'cat': Categories.objects.all(),
        'about_me' :About.objects.all(),
    }
    return render(request,'about.html',context)

def categories(request,categorie):
    context = {
        'post': Post_data.objects.all(),
        'cati': Categories.objects.get(cat=categorie),
        'cat': Categories.objects.all(),
        'post_cat': Post_data.objects.filter(Categorie = Categories.objects.get(cat=categorie)),
        'about_me' :About.objects.all(),
    }
    return render(request,'categories.html',context)
