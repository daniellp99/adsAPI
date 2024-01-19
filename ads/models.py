from django.contrib.auth.models import User
from django.db import models

STATUS_OPTIONS = [
    ("D", "Draft"),
    ("P", "Pending Approval"),
    ("A", "Approved"),
]


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)


class Advertisement(models.Model):
    title = models.CharField(
        max_length=200,
    )
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="advertisements"
    )
    published = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS, default="D")

    class Meta:
        ordering = ["publication_date"]


class Comment(models.Model):
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField()
