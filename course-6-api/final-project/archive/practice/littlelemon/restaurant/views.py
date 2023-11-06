from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from .models import Category
from .models import Cart
from .models import Order
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MenuSerializer
from .serializers import CategorySerializer
from .serializers import MenudaySerializer
from .serializers import UserSerializer
from .serializers import ManagerSerializer
from .serializers import CartSerializer
from .serializers import CartItemsSerializer
from .serializers import OrderSerializer
from .serializers import DeliveryCrewSerializer 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.shortcuts import get_object_or_404
from decimal import Decimal
from datetime import datetime



# from rest_framework import generics

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu':menu_data}
    return render(request, 'menu.html', main_data)

def display_menu_items(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {'menu_item':menu_item})

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serialized_users = UserSerializer(data=request.data)
        serialized_users.is_valid(raise_exception=True)
        serialized_users.save()
        return Response(serialized_users.data, status.HTTP_201_CREATED)
    else:
        return Response({'message': 'You are not authorized to do that'}, 403)    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_users(request):
    if request.user.groups.filter(name='Manager').exists() and request.method == 'GET':
        users = User.objects.all()
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data, status.HTTP_200_OK)
    else:
        return Response({'message': '403 - Unauthorized'}, 403)        

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_user(request, me=None):
    try:
        me = request.user.id
        user = User.objects.get(id=me)
    except User.DoesNotExist:
        return Response({'message': 'This user does not exist'}, status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialized_users = UserSerializer(user)
        return Response(serialized_users.data, status.HTTP_200_OK)
    else:
        return Response({'message': '403 - Unauthorized'}, 403)        

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def category_items(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serialized_categories = CategorySerializer(categories, many=True)
        return Response(serialized_categories.data)
    if request.method == 'POST':
        if request.user.groups.filter(name = 'Admin').exists():
            serialized_categories = CategorySerializer(data=request.data)
            serialized_categories.is_valid(raise_exception=True)
            serialized_categories.save()
            
            return Response(serialized_categories.data, status.HTTP_201_CREATED)
        else:
            return Response({'message': 'You are not authorized to create a new category'}, 403)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def menu_items(request):
    if request.method == 'GET':
        items = Menu.objects.select_related('category').all()
        serialized_items = MenuSerializer(items, many=True)
        return Response(serialized_items.data, status.HTTP_200_OK)
    
    if request.method == 'POST':
        if request.user.groups.filter(name='Manager').exists():
            serialized_items = MenuSerializer(data=request.data)
            serialized_items.is_valid(raise_exception=True)
            serialized_items.save()
            return Response(serialized_items.data, status.HTTP_201_CREATED)
        else:
            return Response({'message': '403 Unauthorized'}, 403)
    if request.method in ['PUT', 'PATCH', 'DELETE']:
        return Response({'message': '403 Unauthorized'}, 403)
            
    else:
        return Response({'message': '403 - Unauthorized'}, 403)
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def single_menu_item(request, menu_id = None):
    try:
        item = Menu.objects.get(pk=menu_id)
    except Menu.DoesNotExist:
        return Response({'message': 'This menu item does not exist'}, status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        seriailized_items = MenuSerializer(item)
        return Response(seriailized_items.data, status.HTTP_200_OK)
    
    if request.method == 'POST':
        if request.user.groups.filter(name='Manager').exists():
            serialized_items = MenuSerializer(item, data=request.data)
            serialized_items.is_valid(raise_exception=True)
            serialized_items.save()
            return Response(serialized_items.data, status.HTTP_200_OK)
        else:
            return Response({'message': '403 - Unauthorized'}, 403)
    
    if request.method == 'PUT':
        if request.user.groups.filter(name='Manager').exists():
            serialized_items = MenuSerializer(item, data=request.data)
            serialized_items.is_valid(raise_exception=True)
            serialized_items.save()
            return Response(serialized_items.data, status.HTTP_200_OK)
        else:
            return Response({'message': '403 - Unauthorized'}, 403)
    
    if request.method == 'PATCH':
        if request.user.groups.filter(name='Manager').exists():
            serialized_items = MenuSerializer(item, data=request.data, partial=True)
            serialized_items.is_valid(raise_exception=True)
            serialized_items.save()
            return Response(serialized_items.data, status.HTTP_200_OK)
        else:
            return Response({'message': '403 - Unauthorized'}, 403)
    
    if request.method == 'DELETE':
        if request.user.groups.filter(name='Manager').exists():
            item.delete()
            return Response({'message': 'Menu item deleted'}, status.HTTP_200_OK)
        else: 
            return Response({'message': '403 - Unauthorized'}, 403)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def manager_set(request):
    # Checking if user is a manager
    if not request.user.groups.filter(name = 'Manager').exists():
        return Response({'message': 'You are not authorized to view the managers'}, 403)
    
    # Check if method is a POST, if so request the username from the request data and check if the user exists otherwise return a 404
    # If the user exists, add the user to the manager group and return a 200 response
    if request.method =='POST':
        serialized_item = ManagerSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        username = serialized_item.validated_data['username']
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        managers.user_set.add(user) # adding Manager to the user group field
        message = 'User {} has been added to the Manager group'.format(username)
        return Response({'message': message}, status.HTTP_200_OK)
    
    elif request.method == 'GET':
        managers = User.objects.filter(groups = Group.objects.get(name='Manager'))
        serialized_item = UserSerializer(managers, many=True)
        return Response(serialized_item.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def manage_delete(request, user_id=None):
    if request.user.groups.filter(name='Manager').exists() and request.method == 'DELETE':
        user = get_object_or_404(User, pk=user_id)
        if user.groups.filter(name='Manager').exists(): # checks if the selected user is a manager or not
            managers = Group.objects.get(name='Manager')
            user.groups.remove(managers) # removes the manager from the user group field
            message = 'User {} has been removed from the Manager group'.format(user.username)
            return Response({'message': message}, status.HTTP_200_OK)
        else:
            return Response({'message': 'This user is not a manager'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'You are not authorized to delete managers'}, status.HTTP_403_FORBIDDEN)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def delivery_crew_set(request):
    # Check if the requested user is a manager
    if not request.user.groups.filter(name = 'Manager').exists():
        return Response({'message': 'You are not authorized to view the managers'}, 403)    
    
    # Check if the method requested is a GET
    if request.method == 'GET':
        # Retrieve all the users a group field of delivery crew 
        # Display the user in a JSON format using the Userserilizer class
        delivery_crew = User.objects.filter(groups = Group.objects.get(name='Delivery crew'))
        serialized_item = UserSerializer(delivery_crew, many=True)
        return Response(serialized_item.data, status.HTTP_200_OK)

    # If the method is a POST, retrieve the data from the requested data via the DeliveryCrewSerializer class (may need to create a new serializer )
    if request.method == 'POST':
        serialized_item = ManagerSerializer(data=request.data)
        # validate the data and retrieve the username from the validated data
        serialized_item.is_valid(raise_exception=True)
        username = serialized_item.validated_data['username']
        # check if the usernmae exists in the database, if not return a 404
        user = get_object_or_404(User, username=username)
        # assign the user a group field of delivery crew
        delivery_crew = Group.objects.get(name="Delivery crew")
        delivery_crew.user_set.add(user)
        # inform the client that the user has been added to the delivery crew group
        message = 'User {} has been added to the Delivery crew group'.format(username)
        return Response({'message': message}, status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delivery_crew_delete(request, user_id=None):
    # Check if the requested user is a Manager and if the request method is DELETE
    if request.user.groups.filter(name='Manager').exists() and request.method == 'DELETE':
        # Retrieve the user using the user_id from the User database
        user = get_object_or_404(User, pk=user_id)
        # Retrieve the group field of the user and check if its a delivery crew 
        if user.groups.filter(name='Delivery crew').exists():
            # remove the user from the delivery crew group
            delivery = Group.objects.get(name='Delivery crew')
            user.groups.remove(delivery) 
            # Display a message to the clietn that the user has been removed from the delivery crew group
            message = 'User {} has been removed from the Delivery crew group'.format(user.username)
            return Response({'message': message}, status.HTTP_200_OK)
        else:
            return Response({'message': 'This user is not a Delivery crew'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'You are not authorized for this action'}, status.HTTP_403_FORBIDDEN)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])    
def cart_set(request):
    # Check if the user is a customer
    # Check if the method is a POST
    if request.method == 'POST':
        # Check to see if the menu item requested exists in the database, if it doesnt return a 404
        menuitem_id = request.data['menuitem_id']
        quantity = request.data['quantity']
        unit_price = Menu.objects.get(pk=menuitem_id).price
        price = Decimal(quantity) * Decimal(unit_price)
        user = request.user.id
        # Create a dictionary with the user's POST data to satisfy the Cart model fields
        data = {
            'user_id': user, 
            'menuitem_id': menuitem_id, 
            'quantity': quantity, 
            'unit_price': unit_price, 
            'price': price
            }
        serialized_items = CartSerializer(data=data)
        serialized_items.is_valid(raise_exception=True)
        serialized_items.save()
        message = 'Menu item has been added to the cart'
        return Response({'message': message}, status.HTTP_201_CREATED)
    if request.method == 'GET':
        items = Cart.objects.filter(user=request.user.id)
        serialized_items = CartItemsSerializer(items, many=True)
        return Response(serialized_items.data, status.HTTP_200_OK)
    else:
        return Response({'message': 'You are not authorized to do that'}, 403)
    
# POST METHOD
# Customer:  Creates a new order item for the current user. Gets current cart items from 
# the cart endpoints and adds those items to the order items table. Then deletes all items from the cart for this user.
# GET METHOD
# Custmer:  Return all orders with order items created by the user 
# Manager:  Return all orders with order items by all users
# Delivery crew:  Return all orders with order items assigned to the delivery crew


# ! IMPORTANT !
# I should create a model for storing the ODER ID that has a one to one relationship with the ORDER ITEM model 
# The ORDER ID shall be issued only when the cart is checked out and the order items are created in the ORDER ITEM model
# That way, each order item is related to a specific oder ID . 
# This ORDER ID Model should have a status field so that it can be set for the delivery crew
# The ORDER ID Model should have a driver assigned field as well

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def order_set(request):
    if request.method == 'POST':
        if Cart.objects.filter(user_id=request.user.id).exists():
            cart = Cart.objects.filter(user=request.user.id)
            user = request.user.id
            for item in cart:
                order_data = {
                    'menuitem': item.menuitem_id,
                    'quantity': item.quantity,
                    'unit_price': item.unit_price,
                    'price': item.price,
                    'user': user,
                    'order_date': datetime.now()
                    }
                serialized_items = OrderSerializer(data=order_data)
                serialized_items.is_valid(raise_exception=True)
                serialized_items.save()
                item.delete()
                message = 'Order has been created'
            
            return Response(message, status.HTTP_201_CREATED)
        else:
            return Response({'message': 'You do not have any items in your cart'}, status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        if request.user.groups.filter(name='Manager').exists():
            manager_view = Order.objects.all()
            serialized_items = OrderSerializer(manager_view, many=True)
            return Response(serialized_items.data, status.HTTP_200_OK)
        else:            
            items = Order.objects.filter(user=request.user.id)
            serialized_items = OrderSerializer(items, many=True)
            return Response(serialized_items.data, status.HTTP_200_OK)
    else:
        return Response({'message': 'You are not authorized to do that'}, 403)
    
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def order_item(request, order_id = None):
    if request.method == 'GET':
        try:
            item = Order.objects.get(pk=order_id)
            # Checkif the user_id of the order item matches the user_id of the request
        
        except Order.DoesNotExist:
            return Response({'message': 'This order item does not exist'}, status.HTTP_404_NOT_FOUND)
        if item.user_id != request.user.id:
            return Response({'message': 'You are not authorized to view this order'}, status.HTTP_403_FORBIDDEN)
        else:
            serialized_items = OrderSerializer(item)
            return Response(serialized_items.data, status.HTTP_200_OK)    
    if request.method == 'PUT':
        # method PATCH & PUT
        # Updates the order. A manager can use this endpoint to set a delivery crew to this order, 
        # and also update the order status to 0 or 1.
        # url: /api/orders/{orderId}
        # The user must provide the Delivery crew user ID and the order status in the request data when accesing the url.
        
        
        # Check if the user is a manager
        if request.user.groups.filter(name='Manager').exists():
            # Check if the order_id exists in the database
            try:
                item = Order.objects.get(pk=order_id)
            except Order.DoesNotExist:
                return Response({'message': 'This order item does not exist'}, status.HTTP_404_NOT_FOUND)
            # Use a new Serializer to validate the data (data should be the delivery crew user id and the order status) (should be linked to Order Model)
            serialized_items = DeliveryCrewSerializer(data=request.data)
            serialized_items.is_valid(raise_exception=True)
            # Check if the user_id is a delivery crew
            if serialized_items.validated_data['user_id'].groups.filter(name='Delivery crew').exists():
                # Update the order with the validated data
                item.status = serialized_items.validated_data['status']
                item.delivery_crew = serialized_items.validated_data['user_id']
                item.save()
                # Return a message and a 200 response
                return Response({'message': 'Order has been updated'}, status.HTTP_200_OK)
            
            # Check if the data is valid
            # Update the order with the validated data
            # Return a messag and a 200 response
            

    
    

    
    
    
    if request.method == 'GET':
        seriailized_items = OrderSerializer(item)
        return Response(seriailized_items.data, status.HTTP_200_OK)
    
    if request.method == 'POST':
        if request.user.groups.filter(name='Manager').exists():
            serialized_items = OrderSerializer(item, data=request.data)
            serialized_items.is_valid(raise_exception=True)
            serialized_items.save()
            return Response(serialized_items.data, status.HTTP_200_OK)
        else:
            return Response({'message': '403 - Unauthorized'}, 403)
    
    if request.method == 'PUT':
        if request.user.groups.filter(name='Manager').exists():
            serialized_items = OrderSerializer(item, data=request.data)
            serialized_items.is_valid(raise_exception=True)
            serialized_items.save()
            return Response(serialized_items.data, status.HTTP_200_OK)
        else:
            return Response({'message': '403 - Unauthorized'}, 403)
    
    if request.method == 'PATCH':
        if request.user.groups.filter(name='Manager').exists():
            serialized_items = OrderSerializer(item, data=request.data, partial=True)
            serialized_items.is_valid(raise_exception=True)
            serialized_items.save()
            return Response(serialized_items.data, status.HTTP_200_OK)
        else:
            return Response({'message': '403 - Unauthorized'}, 403)
    
    if request.method == 'DELETE':
        if request.user.groups.filter(name='Manager').exists():
            item.delete()
            return Response({'message': 'Order item deleted'}, status.HTTP_200_OK)
        else: 
            return Response({'message': '403 - Unauthorized'}, 403)


@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def menu_of_day(request, menu_id=None):
    try:
        item = Menu.objects.get(pk=menu_id)
    except Menu.DoesNotExist:
        return Response({'message': 'This menu item does not exist'}, status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized_items = MenudaySerializer(item)
        return Response(serialized_items.data)
    
    if request.method == 'PATCH':
        if request.user.groups.filter(name='Manager').exists():
            serialized_items = MenudaySerializer(item, data=request.data, partial=True)
            serialized_items.is_valid(raise_exception=True)
            serialized_items.save()
            # serialized_items.validated_data  # If we need to access the data before saving method.            
            return Response(serialized_items.data, status.HTTP_200_OK)
        return Response({'message': 'You are not authorized to update the Menu of the day'}, 403)
    else:
        return Response({'message': 'Only autorhized to view'}, 403)        

