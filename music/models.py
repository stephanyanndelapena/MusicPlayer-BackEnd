

# Create your models here.
from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, blank=True)
    audio_file = models.FileField(upload_to='tracks/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tracks = models.ManyToManyField(Track, related_name='playlists', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name