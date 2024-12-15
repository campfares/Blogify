from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    context = {
        'post': Post_data.objects.all(),
        'cat': Categories.objects.all()
    }
    return render(request,'index.html',context)

def blog_page(request,pk):
    if request.method == "POST":
        name = request.POST['name']
        body = request.POST['body']
        
        new_comment = Comment(name=name,comment_content=body)
        new_comment.save()
    context={
        'post' : Post_data.objects.get(id = pk),
        'comment' : Comment.objects.all()
    }
    
    return render(request,'blocksignal.html',context)

def contact(request):
    context = {
        'cat': Categories.objects.all()
    }
    return render(request,'contact.html',context)

def about(request):
    context = {
        'cat': Categories.objects.all()
    }
    return render(request,'about.html',context)

def categories(request,categorie):
    context = {
        'cati': Categories.objects.get(cat=categorie),
        'cat': Categories.objects.all(),
        'post_cat': Post_data.objects.filter(Categorie = Categories.objects.get(cat=categorie)),
    }
    return render(request,'categories.html',context)
