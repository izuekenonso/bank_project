from django.db import models
from .User import CustomUser
from django.utils import timezone



class Transaction(models.Model):

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank = True, null = True )
    trxn_id = models.CharField(max_length=50, unique=True)
    trxn_type = models.CharField(max_length=50)
    trxn_amount = models.DecimalField(max_digits=19, decimal_places=4)
    timestamp = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.trxn_type