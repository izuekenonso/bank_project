from django.contrib import admin
from .models import CustomUser, Account, Transaction


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_name', 'first_name')


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_number', 'account_balance')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'trxn_id', 'trxn_type', 'trxn_amount')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)