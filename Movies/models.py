from django.db import models
import random
import string
def rand_id():
    id = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    return id
# Create your models here.
class Film(models.Model):
    filmid = models.CharField(name = 'filmid', default=rand_id, max_length=8)
    title = models.TextField(name='title')
    count = models.IntegerField(name = 'count', default=0)
    
class Chapter(models.Model):
    filmid = models.CharField(name = 'filmid', default='********', max_length=8)
    chapterid = models.IntegerField(name='chapterid', default=0)
    url = models.URLField(name='url')
