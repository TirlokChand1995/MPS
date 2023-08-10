from django.db import models

# Create your models here.
class Teachers(models.Model):
    Pic = models.ImageField(upload_to="static",default="Noimage.jpg")
    Name = models.CharField(max_length=50,default="")
    Des = models.CharField(max_length=50,default="Teacher")
    Experience = models.IntegerField(default=0)
    def __str__(self):
        return self.Name
class Gallery_main(models.Model):
    Gal_main = models.ImageField(upload_to="static")

class Gallery(models.Model):
    Gal = models.ImageField(upload_to="static")