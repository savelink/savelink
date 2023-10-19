from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 


class light(models.Model):
  name=models.CharField( max_length=300,null=True,blank=False ,  ) # choices=[(x, x.value) for x in TransactionStatus]
  video=models.FileField(upload_to='videos_uploaded',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
  date=models.DateTimeField(default=datetime.now(), blank=True)
  user=models.OneToOneField( User,on_delete=models.CASCADE )


        
