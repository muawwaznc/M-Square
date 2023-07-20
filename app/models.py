from django.db import models
from django.utils import timezone

class seller(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 11)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 15)
    storename = models.CharField(max_length= 50) 
    earning = models.FloatField(default=0.0)

class buyer(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 11)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 15)

class product(models.Model):
    category = models.CharField(max_length = 20)
    name = models.CharField(max_length = 40)
    quantity = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='static/productImages/')
    sellerID = models.ForeignKey(seller, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=timezone.now)

class cart(models.Model):
    buyerID = models.ForeignKey(buyer, on_delete=models.CASCADE)
    productID = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class orders(models.Model):
    buyerID = models.ForeignKey(buyer, on_delete=models.CASCADE)
    productID = models.ForeignKey(product, on_delete=models.CASCADE)
    sellerID = models.ForeignKey(seller, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    orderedAt = models.DateTimeField(default=timezone.now)
    isDeliver = models.BooleanField(default=False)


