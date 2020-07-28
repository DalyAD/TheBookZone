from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Book(models.Model):
    isbn13 = models.CharField(max_length=254, null=True, blank=True)
    isbn10 = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField(max_length=999999999)
    published_year = models.CharField(max_length=4, default=None)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    num_pages = models.CharField(max_length=6, default=None)
    ratings_count = models.CharField(max_length=999999999, default=None)

    def __str__(self):
        return self.title