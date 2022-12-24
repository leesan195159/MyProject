from django.db import models

from cores.timestamp import TimestampZone

class User(TimestampZone):
    name     = models.CharField(max_length=30)
    email    = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'users'
