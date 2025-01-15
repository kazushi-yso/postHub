from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    uid = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name

class post(models.Model):
    uid = models.CharField(unique=True, max_length=100)
    title =models.CharField(max_length=100)
    content =models.TextField()

    def __str__(self):
        return self.title