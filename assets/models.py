from django.db import models
from django.contrib.auth.models import User


class Asset(models.Model):

    LAPTOP  = 'L'
    PHONE   = 'P'
    MONITOR = 'M'
    TV      = 'T'
    OTHER   = 'O'

    TYPE = [
        (LAPTOP,        'laptop'),
        (PHONE,   'mobile phone'),
        (MONITOR,      'monitor'),
        (TV,                'TV'),
        (OTHER,          'other'),
    ]

    READY     = 'R'
    ASSIGNED  = 'A'
    ON_REPAIR = 'P'
    RETIRED   = 'T'
    LOST      = 'L'
    STOLEN    = 'S'

    STATUS = [
        (READY,     'ready for assignment'),
        (ASSIGNED,              'assigned'),
        (ON_REPAIR,            'on repair'),
        (RETIRED,                'retired'),
        (LOST,                      'lost'),
        (STOLEN,                  'stolen'),
    ]

    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    vendor = models.CharField(max_length=64)
    last_modified = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=512)
    type = models.CharField(max_length=1, choices=TYPE)
    status = models.CharField(max_length=1, choices=STATUS)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Request(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

