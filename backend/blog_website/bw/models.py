from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class Categories(models.Model):
    cat = models.CharField(max_length=50)
    
    def __str__(self):
        return self.cat 

class Post_data(models.Model):
    
    post_img = models.ImageField(upload_to ='uploads',default='static/img/imag_1.jpg')
    title = models.CharField(max_length=200 ,default='notitle' )
    author_name = models.CharField( max_length=50 ,default='anonymous')
    aurthor_photo = models.ImageField( upload_to='author', null=True, blank=True ,default='static/img/imag_1.jpg')
    date = models.DateField(default='timezone')
    content = models.TextField( default='no content to see')
    content_img = models.ImageField( upload_to='content_img',default='there is no content')
    tags = TaggableManager()
    Categorie = models.ForeignKey(Categories, on_delete=models.PROTECT, default='none')

    def return_tags(self):
        taglist = self.tags.names()
        return taglist

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post_comment = models.ForeignKey(Post_data, related_name= "comments" ,on_delete=models.CASCADE, default='none')
    name = models.CharField(max_length=200 ,default="no name")
    date = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField(default="pls be nice")
