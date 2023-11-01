# Ordering

## Django-filter

django-filter is a package that allows you to use advnaced filtering. But this is used for class based views. Since our examples are using functions views with `@api_view` decorators, we can take advantages of django's native sorting methods.

```py
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_views, renderer_classes
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def menu_items(request):
    if (request.method=='GET'):
        items = MenuItem.object.select_related('category').all()
        category_name = request.query_paramsget('category')
        to_price = request.query_param.get('to_price')
        search = request.query_param.get('serach')
        ordering = request.query_params.get('ordering')
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
        if search:
            items = items.filter(title__startswith=search)
        if ordering:
            ordering_fields = odering.split(",") # if the user wants to search more than 1 items ( `http://127.0.0.1:8000/api/menu-items/?ordering=price,inventory`) asc and desc can be done with a negative sign
            items = items.order_by(*ordering_fields) # this is using the  order_by build in parameter function

        serialized_item = MenuItemSerializer(items, many = True)
        return Response(serialized_item.data)
    elif request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data, status.HTTP_201_CREATED)
```
