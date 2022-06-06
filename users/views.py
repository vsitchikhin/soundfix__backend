from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.
class UserAPIView(APIView):
    def get(self, request):
        user_list = User.objects.all().values()
        return Response({'users': list(user_list)})


    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'user': serializer.data})
    