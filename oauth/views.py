from msilib.schema import Error
from os import access
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Oauth
import hashlib
import datetime
from datetime import timezone

# Create your views here.
class GetToken(APIView):
    def post(self, request):
        try: 
            data = request.data
            username = data['username']
            password = data['password']
            grant_type = data['grant_type']
            client_id = data['client_id']
            client_secret = data['client_secret']

            oauth = Oauth.objects.get(username=username, password=password, grant_type=grant_type, client_id=client_id, client_secret=client_secret)
            last_hit = datetime.datetime.now()
            random_time = last_hit + datetime.timedelta(minutes=5)
            to_hash = oauth.username + str(last_hit)
            to_hash2 = oauth.username + str(random_time)
            encoded_str = to_hash.encode()
            encoded_str2 = to_hash2.encode()
            hash_obj = hashlib.sha1(encoded_str)
            hash_obj2 = hashlib.sha1(encoded_str2)
            access_token = hash_obj.hexdigest()
            refresh_token = hash_obj2.hexdigest()
            oauth.access_token= access_token
            oauth.refresh_token= refresh_token
            oauth.save()
            return Response({
                "access_token" : access_token,
                "expires_in": 300,
                "token_type": "Bearer",
                "scoop": None,
                "refresh_token": refresh_token
            }, status=status.HTTP_200_OK)

        except:
            return Response({
                "status": 401,
                "error": "invalid_request",
                "error_description": "ada error mas, cek lagi deh isi suratnya!"
            }, status=status.HTTP_401_UNAUTHORIZED)

class GetResource(APIView):
    def post(self, request):
        try: 
            token = request.headers['Authorization']
            token = token[7:]
            user = Oauth.objects.get(access_token = token)
            now = datetime.datetime.now(timezone.utc)
            interval = (now - user.last_hit).total_seconds()
            if interval > 300:
                return Response({
                    "status": 401,
                    "error": "invalid_token",
                    "error_description": "maaf sepertinya access token sudah expired, silahkan dapatkan yang baru"
                }, status=status.HTTP_401_UNAUTHORIZED)
                
            return Response({
                    "status": 200,
                    "access_token": user.access_token,
                    "client_id": user.client_id,
                    "user_id": user.username,
                    "full_name": user.full_name,
                    "npm": "1906398212",
                    "expires": None,
                    "refresh_token": user.refresh_token
                }, status=status.HTTP_401_UNAUTHORIZED)


        except Exception as e:
            print(e)
            return Response({
                "status": 401,
                "error": "invalid_token",
                "error_description": "sepertinya token salah mas!"
            }, status=status.HTTP_401_UNAUTHORIZED)