## Writing serilaizers with less code

In the code below, we did the following:

- hashed out the old cold
- imported the `MenuItem` model from `models`
- changed the field name `inventory` to `stock` by assigning it to the `stock` variable.
- Craeted a Meta Class which holds the `model` and `fields` variable
- Created a new method to calculate the tax price
- imported the `Decimal` from `decimal`
- Added a new field by creating a variable and linking it to the `calculate_tax` method
- Added the price_after_tax field to the fields arry

Also, if the field names you are going to list consist of all the files, you can use "all" rather than typing all the fields out at once.

serializer.py file

```py
from rest_framework import serializers
from .models import MenuItem
from decimal import Decimal

# class MenuItemSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class MenuItemSerializers(serializers.SErializers):
    stock = serializers.IntegerField(source = 'inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax']
        # fields = '__all__'

    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)

```
