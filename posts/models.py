from django.db import models
from django.contrib.auth import get_user_model


class NewPost(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    caption = models.TextField()

    def __str__(self):
        return self.caption
