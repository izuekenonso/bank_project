from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ..models import Transaction, Account
from ..serializers import AccountSerializer
from django.contrib.auth.hashers import make_password
from ..serializers import TransactionSerializer
from django.db.transaction import atomic
import random
from rest_framework.permissions import IsAuthenticated


class TransactionApiView(APIView):
    
    @atomic
    def post(self, request, *args, **kwargs):

        permission_classes = (IsAuthenticated)

        data = {
            'user': request.data.get('user'),
            'trxn_id': "%s%s" % ( str(request.data.get('user')), str(random.randint(0000, 9999)) ),
            'trxn_type': request.data.get('trxn_type'), 
            'trxn_amount': request.data.get('trxn_amount'),
        }

        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():
            
            serializer.save()

            self.update_user_account_balance(data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def get(self, request, *args, **kwargs):

        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(data=serializer.data)



    def update_user_account_balance(self, trxn_data):

        existing_amount = 0
        new_amount = 0

        trxn_type = trxn_data['trxn_type']
        trxn_amount = float(trxn_data['trxn_amount'])


        account = Account.objects.get(user=trxn_data['user'])

        print("-----=====")
        print(account.account_balance)

        if account is not None:
            serializer = AccountSerializer(account)
            existing_amount = float(serializer.data['account_balance'])

            if (trxn_type == '1'):
                new_amount = existing_amount + trxn_amount
            elif (trxn_type == '2'):
                new_amount = existing_amount - trxn_amount
            else:
                # transfer
                return False


            update_data = {
                'account_balance': new_amount
            }

            serializer = AccountSerializer(instance=account, data=update_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return True
            return False
        return False




class TransactionDetailApiView(APIView):

    def get(self, request, transaction_id, *args, **kwargs):
        
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response({"message":  "%s%s" % ('Could not find transaction with id: ', transaction_id)}, status=status.HTTP_400_BAD_REQUEST)


    

