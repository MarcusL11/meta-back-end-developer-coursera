### Django Rest Framework Summary

### Django Rest Framework (DRF)

- DRF is a toolkit built on top of the Django web framework that allows you to create APIs more efficiently.
- DRF can retrieve data from the database, process it, and then represent it to your clients as JSON, XML, or other formats of data.
- DRF benefits include a built-in API viewer, human readable HTTP status codes, built-in serializers for data conversion, and deserialization for converting user supplied data into models to store in a database.

### Installing and configuring DRF

- You can install DRF with pip.
- Pipenv is a tool that manages virtual environments and dependencies for you. It is recommended over pip for installing DRF.

### API view decorator

- The API view decorator is used to create API endpoints.
- API decorators can help you to quickly prototype, inspect, and test APIs.

### Routers

- Routers are used to auto configure URLs from class based views.
- This means that you don't need to create individual URL patterns for each class method.

### Function and class based views

- Function based views are simple and easy to use, but they can be repetitive and difficult to maintain for complex APIs.
- Class based views are more powerful and flexible, but they can be more complex to implement.

### Serializers

- Serializers are used to convert database models to and from JSON, XML, or other formats of data.
- DRF includes a number of built-in serializers that you can use for common tasks.
- You can also create your own custom serializers.

### Relationships serializers

- Relationships serializers are used to display related data of connected models in the output of your API.

### Deserialization

- Deserialization is the process of converting user supplied data into database models.
- DRF provides a number of built-in deserializers that you can use for common tasks.
- You can also create your own custom deserializers.

### Renderers

- Renderers are responsible for displaying the output of your APIs.
- DRF includes a number of built-in renderers, including JSON, XML, and HTML renderers.
- You can also create your own custom renderers.

### Throttling and caching

- Throttling is used to limit the number of requests that a client can make to your API.
- Caching is used to store the results of API requests so that they can be reused without having to query the database again.

**Conclusion**

Overall, you should be able to:

- Install and set up Django rest framework.
- Use function and class based views to create API endpoints efficiently.
- Create a basic API using DRF serialized database models using model serializers.
- Convert and validate data using serialization.
- Map user input to data based models using deserialization.
- Use throttling and cashing to optimize and protect your API.

## Additional Resources:

[XML renderer, XML support for Django REST framework](https://jpadilla.github.io/django-rest-framework-xml/)
[YAML renderer, YAML support for Django REST framework](https://jpadilla.github.io/django-rest-framework-jsonp/)
[JSONP renderer, JSONP support for Django REST framework](https://jpadilla.github.io/django-rest-framework-yaml/)
