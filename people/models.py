from django.db import models


class Address(models.Model):
    number = models.IntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    STATE_CHOICES = [
        ('NSW', 'New South Wales'),
        ('QLD', 'Queensland'),
        ('VIC', 'Victoria'),
        ('TAS', 'Tasmania'),
        ('NT', 'Northern Territory'),
        ('WA', 'Western Australia'),
        ('SA', 'South Australia'),
    ]
    state = models.CharField(max_length=3, choices=STATE_CHOICES)


class Person(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
