from django.db import models
from django.contrib.auth.models import User , Group
from PIL import Image
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    marker = models.FileField(upload_to='marker/',blank=True, null=True)
    product_model = models.FileField(upload_to='model/',blank=True, null=True)

    @property
    def markerURL(self):
        try:
            url = self.marker.url
        except:
            url = ''

        return url

    @property
    def productModelURL(self):
        try:
            url = self.product_model.url
        except:
            url = ''

        return url

    def __str__(self):
        return self.name
