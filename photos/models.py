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

    def save_image(self):
        self.save()

    class Meta:
        ordering = ['title']

    @classmethod
    def get_images(cls):
        images = cls.objects.all()

        return images

    
    @classmethod
    def get_pics_cat(cls,categ):
        categ_images = cls.objects.filter(category = categ)
        print (categ_images)

        return categ_images

    
    @classmethod
    def photos_by_loct(cls, loct):
        loct_images = cls.objects.filter(location = loct)

        return loct_images

class Category(models.Model):
    cat = models.CharField(max_length = 100)


    @classmethod
    def search_category(cls,search_term):
        category = cls.objects.filter(categ__icontains=search_term)

        return category


class Location(models.Model):
    loct = models.CharField(max_length = 100)

    @classmethod
    def get_location(cls):
        location = cls.objects.all()

        return location

        