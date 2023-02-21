from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=100)

    def request(self):
        return self.name


class Message(models.Model):
    message = models.CharField(max_length=100)

    def request(self):
        return self.message
