import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False,
         name='id')
    name = models.CharField(name = 'name', default='Undefied Name Products', max_length=128)
    description = models.TextField(name = 'description', max_length = 256)
    thumbnail = models.CharField(name = 'thumbnail',max_length = 12)
    details = models.TextField(name = 'details')
    rating = models.FloatField(name = 'rating')
    price = models.FloatField(name = 'price')
    owner = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

