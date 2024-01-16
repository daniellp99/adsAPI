from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Advertisement(models.Model):
    title = models.CharField(
        max_length=200,
    )
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ["publication_date"]


class Comment(models.Model):
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField()
