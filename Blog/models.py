from django.db import models
from django.urls import reverse
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.ImageField(upload_to='profiles')
    date = models.DateField()
        
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('index')



class logindb(models.Model):
    username = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    password = models.CharField(max_length=1000)
    confirmpassword = models.CharField(max_length=1000)

class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment_des = models.CharField(max_length=1000)
    images = models.ImageField(upload_to="profiles")
    

