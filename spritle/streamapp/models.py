from django.db import models
from users.models import StreamUser

# Create your models here.
class Video(models.Model):
    title     = models.CharField(max_length=255)
    video_URL = models.FileField(upload_to='videos/%Y/%m/%d/')
    streamer  = models.ForeignKey(StreamUser,on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.title} with id->{self.id} uploaded by {self.streamer.first_name} {self.streamer.last_name}"