from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Package(models.Model):
    title = models.CharField(max_length=100, unique = True)
    description = models.TextField(null = True)
    price = models.IntegerField(null = True)
    picture = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.title

STATUS = (
    ('QUOTE', 'Quote'),
    ('IN PROCESS', 'In process'),
    ('BOOKED', 'Booked'),
)

class Order(models.Model):
    Customer = models.ForeignKey(User, null = True)
    First_name = models.CharField(max_length=100, null = True)
    Last_name = models.CharField(max_length=100, null = True)
    Date_of_departure = models.DateField(null = True)
    Number_of_travelers = models.IntegerField(null = True)
    Price = models.DecimalField(max_digits=11, decimal_places=2, null = True)
    Package = models.ForeignKey(Package, null = True)
    Departing_city = models.CharField(max_length=100, null = True)
    Destination = models.CharField(max_length=100, null = True, blank = True)
    Status = models.CharField(max_length=100, null = True, blank = True, choices=STATUS, default="QUOTE")
    Notes = models.TextField(null = True, blank = True)

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.First_name, self.Last_name, str(self.Package), self.Status)
