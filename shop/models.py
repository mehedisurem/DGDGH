from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_Name = models.CharField(max_length=270)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    img = models.ImageField(upload_to="shop/images", default="")
    desc = models.TextField()
    pub_date = models.DateField()

 #admin db  table object name set a as product name of that object
    def __str__(self):
        return self.product_Name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30, default="")
    phone = models.CharField(max_length=15, default="")
    desc = models.TextField(default="")


    def __str__(self):
        return self.name