from rest_framework import serializers
from .models import Menu
from .models import Category
from .models import Cart
from django.contrib.auth.models import User 
from django.contrib.auth.models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', ]

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['username', 'id', 'email', 'groups']
        # depth = 1 

    # this line is added to ensure that the password is encrypted when the data is written to the database
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) 
        return user        

class ManagerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, required=True)
    
    class Meta: 
        model = User
        fields = ['username']
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) 
        return user

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price']

class CartSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)    
    
    class Meta:
        model = Cart
        fields = ['menuitem', 'menuitem_id', 'unit_price', 'quantity','price', 'user', 'user_id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'name']

class MenuSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True) # this line is added to allow the category_id to be written to the database, referenncing the ID of the category
    name = serializers.CharField(max_length=200, required=True)
    price = serializers.IntegerField(required=True)
    menu_item_description = serializers.CharField(max_length=1000, required=True)
    menu_of_the_day = serializers.BooleanField(required = True) 
       
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'menu_item_description', 'category', 'category_id', 'menu_of_the_day']
        # depth = 1 # an alternative way coding to display the category data, must remove the category = CategorySerializer() line above

class MenudaySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, read_only=True)
    menu_of_the_day = serializers.BooleanField(required=True)
    class Meta:
        model = Menu
        fields = ['id', 'name', 'menu_of_the_day']
        