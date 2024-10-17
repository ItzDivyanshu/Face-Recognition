from django.db import models

# Create your models here.
class face_data(models.Model):
    username=models.CharField(max_length=100)
    image = models.CharField(max_length=50)

class face_detect(models.Model):
    pic=models.FileField(upload_to='static/image/')

class face_contact(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=50)
    msg = models.CharField(max_length=200)


