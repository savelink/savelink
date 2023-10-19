from rest_framework import serializers
from . import models
class lightSerializer(serializers.ModelSerializer):
    class Meta:
       model = models.light
       fields = ('id', 'name', 'video', 'date', 'user')
