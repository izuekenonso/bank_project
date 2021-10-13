from django.db import models
from .User import CustomUser
from .Account import Account


class Transaction(models.Model):
    DEPOSIT = 1
    WITHDRAWAL = 2
    TRANSFER = 3

    TRANSACTION_TYPE = [
        (DEPOSIT, 'Deposit'),
        (WITHDRAWAL, 'Withdrawal'),
        (TRANSFER, 'Transfer'),
    ]
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank = True, null = True )
    transaction_type = models.CharField(choices=TRANSACTION_TYPE),
    amount = models.DecimalField(max_digits=19, decimal_places=4),
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)



