## views.py

```py
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer

@api_view(['GET', 'POST']) # add post method support
def menu_items(request):
    if request.method == 'GET': #check to see if its a get request
        items = MenuItem.objects.select_related('category').all()
        serialized_item = MenuItemSerializer(items, many = True)
        return Response(serialized_item.data)
    if request.method == 'POST': # check to see if its a post request
        serialized_item = MenuItemSerializer(data=request.data) # deserialized the request data
        serialized_item.is_valid(raise_exception = True) # raise an error if not valid
        # access the valided data using this
        # serialized_item.valudated_data
        serialized.save() # save the data to the database
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view()
def single_item(request, id):
    items = get_object_or_404(MenuItem,pk=id)
    serialized_item = MenuItemSerializer(items)
    return Response(serialized_item.data)

```

### serializers.py

```py
from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializers(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer(read_only = True) # this needs to be read only so that when the user requests to post, its not asking for category.
    category_id = serializers.IntegerField(write_only = True) # for users to define the category data
    class Meta:
        model = MenuItem
        fields = ['data', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']

    def calculate_tax(self, product:MenuItem):
        return product.price*Decimal(1.1)

```
