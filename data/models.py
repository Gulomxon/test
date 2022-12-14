from django.db import models
import time
from user.models import Accaunt

def carusel_location(instance, filename):
    extension   = filename.split('.')[-1]
    name        = time.strftime('%Y_%m_%d%H%M%S')
    return 'images/carusel/%s.%s' % (name, extension)


class Carusel(models.Model):
    user        = models.ForeignKey(Accaunt, on_delete=models.CASCADE, default=1)
    title       = models.CharField(max_length = 150)
    picture     = models.ImageField(upload_to=carusel_location, max_length=100)
    definition  = models.TextField()

    def __str__(self):
        return self.title

def work_location(instance, filename):
    extension   = filename.split('.')[-1]
    mill        = round(time.time() * 1000)
    name        = time.strftime('%Y_%m_%d%H%M%S')
    return 'images/work/%s_%s.%s' % (name, mill, extension)
    
class Work(models.Model):
    user            = models.ForeignKey(Accaunt, on_delete=models.CASCADE)
    title           = models.CharField(max_length = 150)
    picture1        = models.ImageField(upload_to=work_location, max_length=100)
    picture2        = models.ImageField(upload_to=work_location, max_length=100)
    link            = models.URLField()
    technology      = models.TextField()
    active          = models.BooleanField()
    
    def __str__(self):
        return self.title

class Partner(models.Model):
    user            = models.ForeignKey(Accaunt, on_delete=models.CASCADE)
    title           = models.CharField(max_length = 150)
    definition      = models.TextField()
    link            = models.URLField()

    def __str__(self):
        return self.title