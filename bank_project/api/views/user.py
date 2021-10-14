from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ..models import CustomUser
from ..serializers import AccountSerializer
from django.contrib.auth.hashers import make_password
from ..serializers import UserSerializer
from django.db.transaction import atomic



class UserApiView(APIView):
    
    @atomic
    def post(self, request, *args, **kwargs):

        data = {
            'email': request.data.get('email'), 
            'user_name': request.data.get('user_name'), 
            'first_name': request.data.get('first_name'),
            'password': make_password(request.data.get('password')),
            # 'is_superuser': 1,
            # 'is_active': 1,
            # 'is_staff': 1,

        }

        
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            
            user = serializer.save()

            self.create_account(user.id)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def get(self, request, *args, **kwargs):

        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data)



    def create_account(self, userid):

        uid = str(userid)

        account_data = {
                'user': userid,
                'account_number': uid.rjust(5, '0'),
                'account_balance': 0.0
        }


        serializer = AccountSerializer(data=account_data)
        if serializer.is_valid():
            serializer.save()




class UserDetailApiView(APIView):

    def get(self, request, user_id, *args, **kwargs):
        
        try:
            user = CustomUser.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response({"message":  "%s%s" % ('Could not find user with id: ', user_id)}, status=status.HTTP_400_BAD_REQUEST)


    
    def put(self, request, user_id, *args, **kwargs):

        user = CustomUser.objects.get(id=user_id)
        
        if not user:
            return Response({"message":  "%s%s" % ('Could not find user with id: ', user_id)}, status=status.HTTP_400_BAD_REQUEST)


        data = {
            'email': request.data.get('email'), 
            'user_name': request.data.get('user_name'), 
            'first_name': request.data.get('first_name'),
        }

        serializer = UserSerializer(instance=user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, user_id, *agrs, **kwargs):

        user = user = CustomUser.objects.get(id=user_id)

        if not user:
            return Response({"message":  "%s%s" % ('Could not find user with id: ', user_id)}, status=status.HTTP_400_BAD_REQUEST)


        user.delete()
        return Response({"User deleted successfully"}, status=status.HTTP_200_OK)

