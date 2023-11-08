from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=300)
    price = models.IntegerField()
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    img = models.ImageField(upload_to='index/img')
    who = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=300)
    price = models.IntegerField()
    img = models.ImageField(upload_to='Video/img')

    def __str__(self):
        return self.name

class Remot(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=300)
    price = models.IntegerField()
    img = models.ImageField(upload_to='Remot/img')

    def __str__(self):
        return self.name
