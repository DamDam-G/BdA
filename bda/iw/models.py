from django.db import models

class msg(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    msg = models.TextField()
    date = models.DateTimeField()