from django.db import models
import datetime as dt


# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['title']


class Category(models.Model):
    cat = models.CharField(max_length = 100)


class Location(models.Model):
    loct = models.CharField(max_length = 100)