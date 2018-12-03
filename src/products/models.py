import random
import os

from django.db import models

##### Path to image ##################################################################################################################################

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )

# Create your models here.

class Product(models.Model):
    title =  models.CharField(max_length=255)
    dscription = models.TextField()
    price =  models.DecimalField(decimal_places=6, max_digits=20, default=99.99)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    imgdetail = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    category = models.CharField(max_length=255)
    availability = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)

    def __str__(self):
        return self.title
