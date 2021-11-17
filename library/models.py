from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    userid = models.IntegerField(verbose_name="User Id",default=0) 
    def __str__(self):
        return str(self.user)

class AddBook(models.Model):
    name = models.CharField(verbose_name='Book Name',max_length=100,default="")
    author = models.CharField(verbose_name='Author Name',max_length=50,default="")
    isbn = models.CharField(verbose_name='ISBN',max_length=50,default="")
    edition = models.IntegerField(verbose_name="Edition",default=0) 
    pub = models.CharField(verbose_name='Publication Name',max_length=100,default="")
    genres = (
        ('Fiction','Fiction'),
        ('Nonfiction','Nonfiction'),
        ('Romance','Romance'),
        ('Crime and Thriller','Crime and Thriller'),
        ('Religious','Religious'),
        ('Self-help','Self-help'),
        ('Sci-fi','Sci-fi'),
        ('Poetry','Poetry'),
     
    )
    code = models.CharField(verbose_name='Book Code',max_length=50,default="")
    genres=models.CharField(verbose_name='Book Genres',max_length=20,choices=genres,default="")
    def __str__(self):
        return str(self.user)