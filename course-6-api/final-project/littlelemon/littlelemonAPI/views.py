from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from datetime import datetime



# endpoint /api/users
# purpose: create a new user
@api_view(['POST'])
def user(request):
    if request.method == 'POST':
        serialized_user = UserSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        message = {'message': 'User {} created successfully'.format(request.data['username'])}
        return Response(message, status=status.HTTP_201_CREATED)
    else:
        message = {'message': 'request method is not allowed'}
        return Response(message, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# endpoint /api/users/users/me
# purpose: get the current user's information
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userProfile(request, me=None):
    try:
        me = request.user.id
        user = User.objects.get(id=me)
    except User.DoesNotExist:
        return Response({'message': 'This user does not exisit'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)
    else:
        message = {'message': 'request method is not allowed'}
        return Response(message, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
# endpoint /api/groups/mnanager/users
# purpose: Return all managers
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def managerSet(request):
    if request.user.groups.filter(name='Manager').exists() and request.method == 'GET':
        managers = User.objects.filter(groups__name='Manager')
        serialized_managers = UserSerializer(managers, many=True)
        return Response(serialized_managers.data, status=status.HTTP_200_OK)

    elif request.user.groups.filter(name='Manager').exists() and request.method == 'POST':
        serialized_manager = GroupSetSerializer(data=request.data)
        serialized_manager.is_valid(raise_exception=True)
        id = serialized_manager.validated_data['id']
        id = get_object_or_404(User, pk=id)
        manager = Group.objects.get(name="Manager")
        manager.user_set.add(id)
        message = {'message': 'User ID {} has been assigned to Manager Group'.format(request.data['id'])}
        return Response(message, status=status.HTTP_201_CREATED)
    
    else:
        message = {'message': 'Youre not authorized for this action'}
        return Response(message, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# endpoint /api/groups/manager/users/<int:user_id>
# purpose: Remove user from Manager group
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def managerDelete(request, id=None):
    if request.user.groups.filter(name='Manager').exists() and request.method == 'DELETE':
        user = get_object_or_404(User, pk=id)
        if user.groups.filter(name='Manager').exists():
            manager = Group.objects.get(name="Manager")
            user.groups.remove(manager)
            message = {'message': 'User ID {} has been removed from Manager Group'.format(id)}
            return Response(message, status=status.HTTP_200_OK)
        else:
            message = {'message': 'User ID {} is not a Manager'.format(id)}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
    else:
        message = {'message': 'Youre not authorized for this action'}
        return Response(message, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
# endpoint /api/groups/delivery-crew/users
# purpose: Return all delivery crew
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def deliveryCrewSet(request):

    if request.user.groups.filter(name='Manager').exists() and request.method == 'GET':
        delivery_crew = User.objects.filter(groups__name='Delivery crew')
        serialized_delivery_crew = UserSerializer(delivery_crew, many=True)
        return Response(serialized_delivery_crew.data, status=status.HTTP_200_OK)

    elif request.user.groups.filter(name='Manager').exists() and request.method == 'POST':
        serialized_delivery_crew = GroupSetSerializer(data=request.data)
        serialized_delivery_crew.is_valid(raise_exception=True)
        id = serialized_delivery_crew.validated_data['id']
        id = get_object_or_404(User, pk=id)
        delivery_crew = Group.objects.get(name="Delivery crew")
        delivery_crew.user_set.add(id)
        message = {'message': 'User ID {} has been assigned to Delivery Crew Group'.format(request.data['id'])}
        return Response(message, status=status.HTTP_201_CREATED)
    
    else:
        message = {'message': 'Youre not authorized for this action'}
        return Response(message, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# endpoint /api/groups/delivery-crewager/users/<int:user_id>
# purpose: Remove user from Delivery crew group
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deliveryCrewDelete(request, id=None):
    if request.user.groups.filter(name='Manager').exists() and request.method == 'DELETE':
        user = get_object_or_404(User, pk=id)
        if user.groups.filter(name='Delivery crew').exists():
            delivery_crew = Group.objects.get(name="Delivery crew")
            user.groups.remove(delivery_crew)
            message = {'message': 'User ID {} has been removed from Delivery crew Group'.format(id)}
            return Response(message, status=status.HTTP_200_OK)
        else:
            message = {'message': 'User ID {} is not a Delivery crew'.format(id)}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
    else:
        message = {'message': 'Youre not authorized for this action'}
        return Response(message, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# endpoint /api/menu-items
# purpose: Return all menu items and create menu items
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def menu(request):
    if request.method == 'GET':
        menu = Menu.objects.all()
        serialized_menu = MenuSerializer(menu, many=True)
        return Response(serialized_menu.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        if request.user.groups.filter(name='Manager').exists():
            serialized_menu_item = MenuSerializer(data=request.data)
            serialized_menu_item.is_valid(raise_exception=True)
            serialized_menu_item.save()
            message = {'message': 'Menu item {} created successfully'.format(request.data['name'])}
            return Response(message, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Youre not authorized for this action'}, status=status.HTTP_403_FORBIDDEN)    
    else:
        message = {'message': 'request method is not allowed'}
        return Response(message, status=status.HTTP_403_FORBIDDEN)

# endpoint /api/menu-items/<int:menu_id>
# purpose: Return a single menu item, update a single menu item, and delete a single menu item
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def menuItem(request, id=None):
    if request.method == 'GET':
        menu_item = Menu.objects.get(id=id)
        serialized_menu_item = MenuSerializer(menu_item)
        return Response(serialized_menu_item.data, status=status.HTTP_200_OK)
    elif request.method in ['PUT', 'PATCH']:
        if request.user.groups.filter(name='Manager').exists():
            menu_item = Menu.objects.get(id=id)
            serialized_menu_item = MenuSerializer(menu_item, data=request.data, partial=True)
            serialized_menu_item.is_valid(raise_exception=True)
            serialized_menu_item.save()
            message = {'message': 'Menu item updated successfully'}            
            return Response(message, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Youre not authorized for this action'}, status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user.groups.filter(name='Manager').exists():
            menu_item = Menu.objects.get(id=id)
            menu_item.delete()
            message = {'message': 'Menu item {} deleted successfully'.format(id)}
            return Response(message, status=status.HTTP_200_OK)
    else:
        message = {'message': 'request method is not allowed'}
        return Response(message, status=status.HTTP_403_FORBIDDEN)
    
# endpoint /api/cart/menu-items
# purpose: Return all items in the cart of the user, add items to the cart, and delete all items in the cart
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def cart(request):
    if request.method == 'POST':
        serialized_cart = CartItemsSerializer(data=request.data)
        serialized_cart.is_valid(raise_exception=True)
        userId = request.user.id
        userId = get_object_or_404(User, pk=userId)
        itemId = serialized_cart.validated_data['itemId']
        unitPrice = Menu.objects.get(id=itemId).price
        itemId = get_object_or_404(Menu, pk=itemId)
        quantity = serialized_cart.validated_data['quantity']        
        price = unitPrice * quantity
        data = {
            'userId': userId, 
            'itemId': itemId, 
            'quantity': quantity, 
            'unitPrice': unitPrice, 
            'price': price }
        Cart.objects.create(**data)
        message = {'message': 'Menu item {} added to cart successfully'.format(itemId)}    
        return Response(message, status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        userId = request.user.id
        userId = get_object_or_404(User, pk=userId)
        cart = Cart.objects.filter(userId=userId)
        serialized_cart = CartSerializer(cart, many=True)
        return Response(serialized_cart.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        userId = request.user.id
        userId = get_object_or_404(User, pk=userId)
        cart = Cart.objects.filter(userId=userId)
        cart.delete()
        message = {'message': 'All items in cart deleted successfully'}
        return Response(message, status=status.HTTP_200_OK)
    
    else:
        message = {'message': 'request method is not allowed'}
        return Response(message, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
# endpoint /api/orders/
# purpose: {
    # GET: Returns all orders with order items created by this user,
    # POST: Creates a new order for the user.  Gets current items from the cart endpoints and adds to the order items.  Deletes all items from the cart.

# Thought process:
# Check if the user has a cart (if not, return an error message)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def order(request):
    if request.method == 'GET':
        userId = request.user.id
        userId = get_object_or_404(User, pk=userId)
        order = Order.objects.filter(userId=userId)
        serialized_order = OrderSerializer(order, many=True)
        return Response(serialized_order.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        userId = request.user.id
        userId = get_object_or_404(User, pk=userId)
        cart = Cart.objects.filter(userId=userId)
        if cart:
            total_price = 0
            for item in cart:
                total_price += item.price
            data = {
                'userId': userId, 
                'orderDate': datetime.now(), 
                'totalPrice': total_price, 
                'status': 'Pending', 
                'deliveryId': 0, 
                }
            Order.objects.create(**data)
            order = Order.objects.filter(userId=userId).order_by('-id')[0]
            cart = Cart.objects.filter(userId=userId)
            for item in cart:
                data = {
                    'userId': userId,
                    'itemId': item.itemId, 
                    'orderId': order, 
                    'quantity': item.quantity, 
                    'unitPrice': item.unitPrice, 
                    'price': item.price }
                OrderItem.objects.create(**data)
            cart.delete()
            message = {'message': 'Order created successfully'}
            return Response(message, status=status.HTTP_201_CREATED)
        else:
            message = {'message': 'Cart is empty'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    else:
        message = {'message': 'request method is not allowed'}
        return Response(message, status=status.HTTP_405_METHOD_NOT_ALLOWED)
# Get all items from the cart that belong to the user
# Sum up the price of all items in the cart and save it to a variable called total_price
# Create a new order for the user in the Order table (order_date, user_id, order_status, total_price, delivery_crew_id) 
# delete all items from the cart that belong to the user


# endpoint /api/orders/{orderId}
# purpose: 