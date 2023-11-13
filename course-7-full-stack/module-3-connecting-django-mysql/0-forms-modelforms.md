## Notes

**Django forms**

- Forms are the primary elements of user interactivity on the Web.
- Django provides an easy way to generate forms using a form API and model form class.

**Benefits of using Django forms**

- Easier to maintain and manage changes to the form.
- Django handles the names of inputs matching with the server-side code.
- ModelForm can automatically save received data to the database.

**Creating a Django form class**

1. Create a class that inherits from `forms.Form`.
2. Define all the expected attributes that will be passed down in the request.
3. Use the `forms.CharField`, `forms.IntegerField`, `forms.FloatField`, and other field classes to represent the HTML input elements.
4. Use the `metaclass` to define additional settings for the form, such as the validation rules.

**Creating a Django ModelForm**

1. Create a class that inherits from `ModelForm`.
2. Pass the model class that you want to bind with your form to the `ModelForm` constructor.
3. Add implementation details for using a metaclass.

**Handling form data in the view**

1. Create an instance of the form class.
2. Check if the form is valid.
3. If the form is valid, save the data to the database.

**Available form field types**

- `forms.CharField`: Translates to the HTML text input type.
- `forms.IntegerField`: Translates to the HTML text input type, but is customized to accept only integer numbers.
- `forms.FloatField`: Translates to a text input field that validates if the input is a valid float number.
- `forms.FileField`: Translates to the file upload input type on the HTML form.
- `forms.EmailField`: Translates to a charField that validates if the text entered is a valid email ID.
- `forms.ChoiceField`: Translates to an HTML form select element.

**Conclusion**

Django forms provide a powerful and flexible way to create and manage forms in web applications. By using Django forms, you can save time and effort, and create more robust and user-friendly forms.
