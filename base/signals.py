from django.db.models.signals import post_save, post_delete
from .models import Artist
from django.contrib.auth.models import User


def createArtist(sender, instance, created, **kwargs):
    if created:
        user = instance
        Artist.objects.create(
            name=user.username,
            user=user
        )


post_save.connect(createArtist, sender=User)
