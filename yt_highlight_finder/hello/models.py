from django.db import models

class Hello(models.Model):
    videoid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    video = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title