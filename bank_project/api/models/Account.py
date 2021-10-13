from django.db import models
from .User import CustomUser


class Account(models.Model):

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank = True, null = True )
    account_number = models.CharField(max_length=50, unique=True)
    account_balance = models.DecimalField(max_digits=19, decimal_places=4)
    

    def __str__(self):
        return self.account_number