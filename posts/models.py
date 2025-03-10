from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from socialproject.storage_backends import AzureMediaStorage


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='images/%y/%m/%d', storage=AzureMediaStorage(), blank=True)
    caption = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='posts_liked', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def likes_count(self):
        return self.liked_by.count()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    posted_by = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body
