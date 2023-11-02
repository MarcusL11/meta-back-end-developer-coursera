from django.db import models
# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name

class Category(models.Model):
   slug = models.SlugField()
   name = models.CharField(max_length=200)
   
   def __str__(self) -> str:
      return self.name

class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.DecimalField(max_digits=6, decimal_places=2)
   inventory = models.SmallIntegerField(default=0)
   menu_item_description = models.CharField(max_length=1000, default='')
   category = models.ForeignKey('Category', on_delete = models.PROTECT, default = 1)
   menu_of_the_day = models.BooleanField(default=False)
   
   def __str__(self):
      return self.name

class Cart(models.Model):
   user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
   menuitem = models.ForeignKey('Menu', on_delete = models.CASCADE)
   quantity = models.SmallIntegerField(default=1)
   unit_price = models.DecimalField(max_digits=6, decimal_places=2)
   price = models.DecimalField(max_digits=6, decimal_places=2)
   
   def __str__(self):
      return self.menuitem.name + ' ' + str(self.quantity)

      
   
