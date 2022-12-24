from django.db import models

from cores.timestamp import TimestampZone
from users.models import User


class AccountBook(TimestampZone):
    user          = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    amount        = models.IntegerField()
    amount_detail = models.CharField(max_length=200)
    note_content  = models.CharField(max_length=200, null=True)
    url           = models.CharField(max_length=300, null=True)

    class Meta:
        db_table = 'account_book'
