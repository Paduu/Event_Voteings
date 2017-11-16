from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        Token.objects.create(user=instance)

# Create your models here .
class Event(models.Model):
    name = models.CharField(max_length=40)
    eventDate = models.DateTimeField()
    description = models.TextField(blank=True, default='')
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)

class Game(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True, default='')
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)

class Voteing(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    creator = models.ForeignKey('auth.User', related_name='voteings', on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)

