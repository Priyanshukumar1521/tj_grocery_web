from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name