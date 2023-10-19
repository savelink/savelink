
from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


# Create your views here.


class lightView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = models.light.objects.all()
    serializer_class = serializers.lightSerializer
