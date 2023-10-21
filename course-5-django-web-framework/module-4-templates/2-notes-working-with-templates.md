# Working with Tempaltes

## Terminology

## Variables

Variables are these: {{variables}}

- They retrun a dictionary object
- In the folloing example, the variable of {{restaurant}} would return "The Little Lemon"

```
{restaurant : "The Little Lemon"}
```

- This can be done using whats called a dot notation"

```
{{my_dict.key}}
{{my_object.attribute}}
{{my_list.0}}
```

## Tags

### IF function Tag

```html
{% If loggedIn %}
    <span>Hello {{user.name}}</spand>

{% else %}
    <a href="{% url 'login' %}">Login</a>

{% endif %}
```

### Example listing menu items from a list using

### Static Menu Example:

```html
<ul>
  <li>Pasta $8.99</li>
  <li>Pasta $8.99</li>
  <li>Pasta $8.99</li>
  <li>Pasta $8.99</li>
</ul>
```

### Dynamic Menu Example:

```html
<ul>
  {% for items in menu_list %}

  <li>{{item.name}} {{item.price}}</li>

  {% endfor %}
</ul>
```

## Anthoer example

```py
def myview(request):
    langs = ['Python', 'Java', 'PHP', 'Ruby', 'Rust']
    return render(request, 'langs.html', {'langs':langs})
```

```html
{% for key, value in data.items %} {{ key }}: {{ value }} {% endfor %}
```

## Filters

- String upper: {{string|upper}}
- Argument: {{todays_date|date:"Y-m-d"}}

## Comments

```html
{% comment "option_note %} This is a comment {% end of comment %}
```

## Template Inheretence

- This is how to ensure the blocks are reusred across all pages.
- There are 2 tags; **Include** and **Extend**

**Include**

- Include rendering a template in the current context

**Extends**

- Extends creates a parent and child relationship where parent's functionality can be overwritten

### Include

```h
{% include "_header.html" %}

<h1>About Us</h1>

{% include "_footer.html" %}
```

### Include Tag "with"

Include tags will allow you to pass on an objects that contains the information name.

base.html

```py
def about(request):
  return render(request, 'about.html', {"pgname": 'About us'})
```

```h
{% include "_header.html" with pgname=pgname %}
```

### Extends

Can be used in 2 ways;

```h
{% extends "base.html" %}
{% extends variable %}
```
