
# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import InfoSerializer
from .models import Informacion

class InformacionAPIView(generics.RetrieveAPIView):
    lookup_field="id"
    queryset=Informacion.objects.all()
    serializer_class=InfoSerializer