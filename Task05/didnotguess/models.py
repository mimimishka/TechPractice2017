from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RequestType(models.Model):
    typename = models.CharField(max_length=100)
    
class UserRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(RequestType, on_delete=models.CASCADE)
    request_date = models.DateTimeField('request date')