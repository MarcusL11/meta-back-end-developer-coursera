from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from .models import Category
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MenuSerializer
from .serializers import CategorySerializer
from .serializers import MenudaySerializer
from .serializers import UserSerializer
from .serializers import ManagerSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.shortcuts import get_object_or_404



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
        managers.user_set.add(user)
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
        if user.groups.filter(name='Manager').exists():
            managers = Group.objects.get(name='Manager')
            user.groups.remove(managers)
            message = 'User {} has been removed from the Manager group'.format(user.username)
            return Response({'message': message}, status.HTTP_200_OK)
        else:
            return Response({'message': 'This user is not a manager'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'You are not authorized to delete managers'}, status.HTTP_403_FORBIDDEN)

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

