from django.db import models

class msg(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    msg = models.TextField()
    date = models.DateTimeField()

class member(models.Model):
    id = models.AutoField(primary_key=True)
    pseudo = models.TextField()
    email = models.EmailField()
    pwd = models.TextField()
    co = models.BooleanField()
    img = models.TextField()