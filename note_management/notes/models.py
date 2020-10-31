from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=1024)
    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    def __str__(self):
        return self.username
