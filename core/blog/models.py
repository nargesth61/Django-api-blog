from django.db import models
from accounts.models import Profile
from django.urls import reverse

class Posts(models.Model):
    """
    this is a class to define posts for blogs 
    """
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image = models.ImageField(null= True,blank=True)
    title = models.CharField(max_length=400)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null= True)

    created_date = models.DateTimeField(auto_now_add=True)
    upteted_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    

    

            
class Category(models.Model):
    """
    this ia a class to create category for posts
    """
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name