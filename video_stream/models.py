from django.db.models.deletion import CASCADE
from web_stream.settings import MEDIA_ROOT
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.


class Video(models.Model):
    video = models.FileField(upload_to='video/%d')
    title = models.TextField(max_length=100, null=False, verbose_name='title',
                             blank=False, default='Course Video')
    poster = models.ImageField(upload_to='posters')
    slug = models.SlugField(null=False, unique=True)
    posted = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(max_length=3000, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    videoLength = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Video, self).save(*args, **kwargs)


class VideoResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forVideo = models.ForeignKey(Video, null=True, on_delete=CASCADE)
    response = models.TextField(max_length=500)
    responded = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)
