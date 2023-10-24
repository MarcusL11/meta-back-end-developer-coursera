# Different types of routing in DRF

## How to Example

Create a django project as you normally would with an applicaiton.

1. Then install the Django Rest Frameowrk using this command:

```
pip3 install djangorestframework
```

2. Configure your Project's setting file to include the Django Rest Framework

Project > settings.py > INSTALLED_APPS

```
rest_framework
```

To allow a POST request using the DRF, you can adjust the view function like so;

```py
@api_view(['POST'])
def books(requests):
    return Response('list of the books', status=status.HTTP_200_OK)
```

the @api_view decorator allows the polished interface and also allows you to specify which HTTPs to support. We can make it bot for GET and POST like so.

```py
@api_view(['GET','POST'])
def books(requests):
    return Response('list of the books', status=status.HTTP_200_OK)
```

## Routing to a class method

If you map a specific method from a class, then you need to declare that method as a @staticmethod first. After that, you can map it in the urls.py file. Here’s an example of a class in the views.py file.

```py
class Orders():
	@staticmethod
	@api_view()
	def listOrders(request):
    	return Response({'message':'list of orders'}, 200)
```

You can also map this listOrders method in the urls.py file as follows.

```py
from django.urls import path
from . import views
urlpatterns = [
	path('orders', views.Orders.listOrders)
]
```

## Routing class-based views

You can save a lot of time in DRF by mapping a class that extends the APIview. You don’t need to individually map every method of such classes. In an upcoming video, Function and class-based views, you will learn that such classes have HTTP verb-specific methods inside them. When a class extends APIview or generic views, you can simply map those classes in the urls.py file.

Here’s the code of the class that extends the APIView.

```py
class BookView(APIView):
	def get(self, request, pk):
    	return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
	def put(self, request, pk):
    	return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
```

And here is how you map this class in the urls.py file. All you have to do is map the class as a view against an endpoint.

```py
from django.urls import path
from . import views
urlpatterns = [
    path('books/<int:pk>',views.BookView.as_view())
]
```

Now you can make HTTP, GET and PUT calls to the `/api/books/{bookId}` endpoint without issues. If the class has `post()`, `delete()` and `patch()` methods, it will work with HTTP POST, DELETE and PATCH methods too.

## Routing classes that extend viewsets

You can have classes that extend the different types of ViewSets in your API project. Just like the classes that extend APIView, these classes also have specific methods used to respond to different types of HTTP requests. Here’s an example of a typical class that extends the viewset.Viewset class.

```py
Class BookView(viewsets.ViewSet):
	def list(self, request):
    	return Response({"message":"All books"}, status.HTTP_200_OK)
	def create(self, request):
    	return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
	def update(self, request, pk=None):
    	return Response({"message":"Updating a book"}, status.HTTP_200_OK)
	def retrieve(self, request, pk=None):
    	return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
	def partial_update(self, request, pk=None):
        return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
	def destroy(self, request, pk=None):
    	return Response({"message":"Deleting a book"}, status.HTTP_200_OK)
```

You can map this class in the urls.py file in your Django app as follows.

```py
urlpatterns = [
	path('books', views.BookView.as_view(
    	{
        	'get': 'list',
        	'post': 'create',
    	})
	),
    path('books/<int:pk>',views.BookView.as_view(
    	{
        	'get': 'retrieve',
        	'put': 'update',
        	'patch': 'partial_update',
        	'delete': 'destroy',
    	})
	)
]
```

Notice how the HTTP verbs are mapped with each method in this class. Also, note that both the list() and retrieve() methods are present. The list() method is used to display all books, and the retrieve() method is used to display a single book.

After this mapping, you can access the http://127.0.0.1:8000/api/books endpoint with GET and POST methods. While you can access the http://127.0.0.1:8000/api/books/1 endpoint with GET, PUT, PATCH and DELETE.

## Routing with SimpleRouter class in DRF

If you have a class that extends ViewSets then you can use different types of built-in routers to map those classes in your urls.py file. Doing things this way means you don’t have to map the individual methods as you did in the previous section. Initiate a SimpleRouter object and map the class in the urls.py file in your Django app as follows.

```py
from rest_framework.routers import SimpleRouter
router = SimpleRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls
```

After mapping, you can access the api/books and api/books/1 endpoints with the same methods as in the previous example.

Did you notice that the argument trailing_slash=False was passed, instantiating the SimpleRouter object? Without this argument, your API endpoints will have a trailing slash. And, since you don’t want a trailing slash at the end of your API endpoints, you have to pass this argument.

## Routing with DefaultRouter class in DRF

There is another type of router called DefaultRouter which provides an extra benefit over the SimpleRouter. It creates an API root endpoint with a trailing slash that displays all your API endpoints in one place. You can use it this way in the urls.py file.

```py
from rest_framework.routers import DefaultRouter
router = DefaultRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls
```

Again, after mapping, you can access the api/books and api/books/1 endpoints with the same methods as in the previous examples.

Additionally, you can access the API root view when you visit the http://127.0.0.1:8000/api/ endpoint. This will display all the available endpoints as in the screenshot below.
