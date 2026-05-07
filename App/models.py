from django.db import models


# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class AdminUser(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Product(models.Model):
    image = models.ImageField()
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    description = models.TextField()
    price = models.DecimalField(max_digits=1000, decimal_places=2)

    def __str__(self):
        return self.product_name


class Delivery(models.Model):
    DELIVERY_CHOICES = [
        ("1H", "1 Hour"),
        ("21H", "21 Hours"),
        ("27H", "27 Hours"),
    ]

    address = models.TextField()
    zip = models.IntegerField()
    del_time = models.CharField(max_length=3, choices=DELIVERY_CHOICES)

    def __str__(self):
        return f"{self.address} - {self.zip} - {self.get_del_time_display()}"
