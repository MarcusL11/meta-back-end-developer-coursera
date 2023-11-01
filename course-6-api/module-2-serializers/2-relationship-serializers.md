# Relationship Serializers

Using the relationship serializers to display related data in API output

Lets start with the `Model.py ` file where we create the MenuItem models.

We will create a new Cateogry model with a slug and title fields and then connected it to the MenuItem model:

```py

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length = 255)

class MenuItems(models.Model):
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 6, decimal_places =2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT, default = 1)
```

When creating a ForeignKey, you have to make sure that the category cannot be deleted before all the related menu items are deleted first. This is done using `on_delete=models.PROTECT`

In Django, besides PROTECT, there are several other built-in options for the on_delete parameter of a ForeignKey field. Some of the commonly used options are:

1. CASCADE: This option will delete the related objects when the referenced object is deleted.
2. SET_NULL: This option will set the foreign key to NULL when the referenced object is deleted.
3. SET_DEFAULT: This option will set the foreign key to its default value when the referenced object is deleted.
4. SET(): This option allows you to specify a value or a callable that will be used to set the foreign key when the referenced object is deleted.
5. DO_NOTHING: This option will do nothing when the referenced object is deleted. It is important to handle the situation manually to avoid integrity errors.

These options provide flexibility in handling the deletion of related objects when the referenced object is deleted.

Now, lets migrate to update the database with these new changes.

Next, we'll have to add the fields to the serializers fields lists.

```py
class MenuItemSerializers(serializers.SErializers):
    stock = serializers.IntegerField(source = 'inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']


    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
```

Now the category id will be showed:

```js
[
  {
    id: 1,
    title: "Chocolate Cake",
    category: 1,
  },
];
```

Now if we want to display the category name using the serializers in the DRF, we can add the Cateogry model to the seralizers file and add the Category to the MenuItemSerializers class and use the `StringRelatedFiled` built in function. Also, before this, you should make sure that you have instructed the models file to display the fields in string value:

models.py

```py

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length = 255)

    def __str__(self) -> str:
        return self.title

class MenuItems(models.Model):
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 6, decimal_places =2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default = 1)
```

serializers.py

```py
from .models import Category

class MenuItemSerializers(serializers.SErializers):
    stock = serializers.IntegerField(source = 'inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    cateogry = serializers.StringRelatedFiled()
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']


    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)

```

Lastly, when you are converting your a connected model to string, you need to change your view file to load the related model in a single SQL call.

This will make your API more efficient by not running a separate SQl qurery for every item to load the related data.

`items = MenuItem.objects.all() ---> items = MenuItem.objects.select_related('category').all()

```py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSeriazlier

@api_view()
def menu_items(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerializer(items, many = true)
    return Response(serialized_item.data)

@api_view()
def single_items(request, id):
    items = MenuItem.objects.get(pk=id)
    serialized_item = MenuItemSerializer(items)
    return Response(serialized_item.data)
```

Now the category id will be like so:

```js
[
  {
    id: 1,
    title: "Chocolate Cake",
    category: Icecream,
  },
];
```

Now lets use a separate serializer for the category to make it more details.

Open the serializer file and add a new serializer class and remove the serializers.StringRelatedField() built in function and add in the category serialiser instead.

serializers.py

```py
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'tittle']


class MenuItemSerializers(serializers.SErializers):
    stock = serializers.IntegerField(source = 'inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    cateogry = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']


    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)

```

Now things will be displayed like so:

```js
[
  {
    id: 1,
    title: "Chocolate Cake",
    category: {
        'id', 1,
        'slug', "icecream",
        'title', "Icecream"
    },
  }
];
```

## Nested fields

If you were to visit the menu-items endpoint, you would note the category displays as a nested field with its id, title, and slug

Another way to achieve this is using `depth: 1`

Instead of declaring the category field as CategorySerializer you can specify that depth=1 is in the Meta class in MenuItemSerializer. This way, all relationships in this serializer will display every field related to that model. You can change the code of the MenuItemSerializer as below.

```py
class MenuItemSerializer(serializers.ModelSerializer):
    stock =  serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    # category = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category']
        depth = 1
   
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
```

Note the commented line, category = CategorySerializer(). And the new line, depth = 1, was added in the Meta class. Now, if you were to visit the menu items endpoint at http://127.0.0.1:8000/api/menu-items you’d note that the output is exactly the same as it was before.

Displaying nested fields this way provides more information. It also reduces the amount of code the client application developers need to write. This is because they don't have to make separate API calls to retrieve the details for those nested fields anymore.
