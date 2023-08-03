from django.db import models
from django.contrib.auth.models import User


# class Category(models.Model):
#     name= models.CharField(max_length=255)
#     def __str__(self):
#         return self.name
    
class Topic(models.Model):
    name= models.CharField(max_length=255)
    def __str__(self):
        return self.name

# Create your models here.
class Room(models.Model):
    host=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    topic=models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    name= models.CharField(max_length=255)
    description= models.TextField(null=True, blank=True)
    # participants=
    # category=
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    name= models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    body = models.TextField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = ['-created', '-updated']

    def __str__(self):
        return self.body[0:50]