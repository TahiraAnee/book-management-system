from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    published_year = models.CharField(max_length=100)

    def __str__(self):
        return self.title
