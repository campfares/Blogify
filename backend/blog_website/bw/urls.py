from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('categories/<str:categorie>',views.categories,name='cati'),
    path('blog/<int:pk>',views.blog_page,name = 'blog_page')
]
