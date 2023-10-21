# Template examples

In Django, you could write your html as a string of `HttpResponse` like so:

```py
from django.http import HttpResponse
def index(request):
return HttpResponse("<h1>Hello, world. </h1>")
```

By you could also use an argument of a function like so:

```py
from django.http import HttpResponse
def index(request, name):
return HttpResponse("<h1>Hello, {}. </h1>".format(name))
```

## Django Template Language or (DTL)

- Create a hello.html file in Django's Project `BASE_DIR`

```html
<html>
  <head>
    <title>My django website</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

## Rendering Template

```py
from django.http import HttpResponse
from django.template import loader
def index(request):
template = loader.get_template('hello.html')
context={}
return HttpResponse(template.render(context, request))
```

If it seems slightly complicated, Django provides a shortcut method called render(). It eliminates the HttpResponse and loader classes.

```py
from django.shortcuts import render
return render(request, 'hello.html', {})
```

## Variable tag

In the above code, the render() function’s third parameter is an empty dictionary object. It is called the template context. You should pass the path parameter as a context to hello.html.

```py
from django.shortcuts import render
def index(request, name):
    context={"name":name}
    return render(request, 'hello.html', context)
```

`Request, Path, Dictionary Variable`

Modify the hello.html file by replacing World with the Django variable syntax. Put the key of the context dictionary name inside double curly brackets as in {{ name }}.

```html
<html>
  <body>
    <h1>Hello {{ name }}</h1>
  </body>
</html>
```

You can use `{% if %}` tag of DTL to implement a conditional logic inside the template. Similarly, with `{% for%}` and `{% endfor %}` tags, a looping construct can be built in the template, which may be useful to display records from a database table on the web page. Django’s Template Language has many more tags. You’ll explore this in a subsequent lesson.

## Filter

```
{{ variable_name | filter_name }}
```

Here are some filters in action. The index() view in the above examples receives a name parameter, and it is rendered in the template with the {{ name }} expression tag. If you apply the upper filter to it, the name will be rendered in uppercase.

## Upper

```
{{ name | upper }}
```

As a result, if the path parameter passed to the view is John, it will be rendered as JOHN.

## Length

The length filter works with a list and returns the number of items in it. The view passes a list as a context to the template: nums=[1,2,3,4]
The template filter {{ nums | length }} outputs 4

## Wordcount

The wordcount filter is similar. It tells you how many words are present in the template variable that has to be a string. For example:

String = 'Simple is better than complex'

is passed a context,

{{ string | wordcount }} returns 5.

## Slicer

The slice filter resembles Python’s slice operator, which separates a part of the given list object. So, if:

nums = [1,2,3,4,5,6,7,8]

Is passed in the context,

{{ nums | slice[1:3] }}

It returns [2,3] and then you can iterate over it.

The first and last filters return the first and last item in the list.

## Static files

**Static files**

The next part of this lab will explore another useful component of Django: Adding static files to the website.

The static image `dessert.jpg` that you will use is already added inside the app directory under the `myapp/static` folder and you can use it once you configure the settings.

**Step 12:**
Open the 'settings.py' file, and add a declaration for the list called `STATICFILES_DIRS` with the following value:

```
'myapp/static',
```

**Tip:** Make sure you add a comma after the string.

**Step 13:**
In the left explorer pane of VS Code inside the myapp folder, expand the `static` folder. Expand the `img` folder and notice that an image file with the name of `dessert.jpg` is present.

Open the `menu.html` file and add the following code below \<!-- Add image code --\>

```
<!-- Add image code -->
<img src="{% static 'img/dessert.jpg' %}">

```

**Tip:** To place an image from the static folder inside a Django template file, make sure to place the following code at the beginning of the HTML file that references the static content.

```
{% load static %}
```

**Tip:** To place an image from the static folder inside a Django template file, use the HTML \<img\> tag and inside the `href=""` attribute, place the Django `{% static %}` and specify the path the image you want to load.

## Conclusion : Steps to creating a template

1. Create a view that defines the render function in the `views.py`
2. Update the url configureations in the list of patterns `urls.py`
3. configure the settings for templates and installed apps `settings.py`
4. Create a HTML page that contains static and dynamic using the DTL `{}`
5. make sure you pass the name of the template page in as arguments inside the render function in `views.py`
