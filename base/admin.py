from django.contrib import admin
from .models import Genre, Album, Song, Artist, Playlist

admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Playlist)

