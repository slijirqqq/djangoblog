from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    Post_title = models.CharField(max_length=50)
    Post_pub_date = models.DateTimeField(default=now)
    Post_text = models.TextField(max_length=300)
    Post_image = models.ImageField(upload_to='event_images/')

    def get_summary(self):
        text = self.Post_text
        if len(text) > 70:
            return self.Post_text[:60] + "..."
        else:
            return self.Post_text
