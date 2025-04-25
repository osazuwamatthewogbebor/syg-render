from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    youtube_url = models.URLField()
    youtube_id = models.CharField(max_length=20, default='O4MV5BRv-ps')  

    def __str__(self):
        return self.title
