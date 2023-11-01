# Pagination

```py
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.core.paginator import Paginator, EmptyPage # import the Paginator builtin function

@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_param.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('searc')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default = 2) # Query parameters to define the items per page
        page = request.query_params.get('page', default = 1) # Query parameters to define the page

        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price=to_price)
        if search :
            items = items.filter(title__contains = search)
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*orderin_filds)

        paginator = Paginator(items, per_page=perpage) # define the paginator variable as the Paginator function with the perpage args
        # this must be a try block in case the user sends a bad requests.
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []
        serialized_item = MenuItemSerializer(items, many = True)
        return Response(serialized_item.data)

    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception = True)
        serialized.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view()
def single_item(request, id):
    items = get_object_or_404(MenuItem,pk=id)
    serialized_item = MenuItemSerializer(items)
    return Response(serialized_item.data)

```
