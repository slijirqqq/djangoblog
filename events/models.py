from django.db import models


class Events(models.Model):
    Event_image = models.ImageField(upload_to='event_images/')
    Event_text = models.CharField(max_length=200)
