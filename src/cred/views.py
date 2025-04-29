from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CredSerializer
from .models import Cred
# Create your views here.

class CredViewSet(viewsets.ModelViewSet):
    queryset = Cred.objects.filter()
    serializer_class = CredSerializer


