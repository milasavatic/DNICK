from django.db import models


# Create your models here.
class PublishingHouse(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    year = models.IntegerField()
    website = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.city} {self.country} {self.year} {self.website}"


class Book(models.Model):
    TYPE_CHOICES = [
        ("S", "SOFT"),
        ("H", "HARD")
    ]
    CATEGORY_CHOICES = [
        ("ROM", "ROMANCE"),
        ("THR", "THRILLER"),
        ("BIO", "BIOGRAPHY"),
        ("CLA", "CLASSIC"),
        ("DRA", "DRAMA"),
        ("HIS", "HISTORY")
    ]

    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="book_photos/", null=True, blank=True)
    isbn = models.IntegerField()
    yop = models.DateField()
    ph = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)
    pageNum = models.IntegerField()
    dimensions = models.IntegerField()
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    cat = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.title} {self.isbn} {self.pageNum} {self.type} {self.cat} {self.price}"
