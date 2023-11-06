from django.db import models


# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name

class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField()
   menu_item_description = models.CharField(max_length=1000, default='')
   
   def __str__(self):
      return self.name
   
class Cart(models.Model):
   userId = models.ForeignKey('auth.User', on_delete = models.CASCADE)
   itemId = models.ForeignKey('Menu', on_delete = models.CASCADE)
   quantity = models.IntegerField(default=1)
   unitPrice = models.DecimalField(max_digits=6, decimal_places=2)
   price = models.DecimalField(max_digits=6, decimal_places=2)
   
class Order(models.Model):
   userId = models.ForeignKey('auth.User', on_delete = models.CASCADE)
   orderDate = models.DateTimeField()
   totalPrice = models.DecimalField(max_digits=6, decimal_places=2, default=0)
   status = models.CharField(max_length=200)
   deliveryId = models.IntegerField()

class OrderItem(models.Model):
   userId = models.ForeignKey('auth.User', on_delete = models.CASCADE)
   itemId = models.ForeignKey('Menu', on_delete = models.CASCADE)
   orderId = models.ForeignKey('Order', on_delete = models.CASCADE, default=1)
   quantity = models.IntegerField(default=1)
   unitPrice = models.DecimalField(max_digits=6, decimal_places=2)
   price = models.DecimalField(max_digits=6, decimal_places=2)
   

   