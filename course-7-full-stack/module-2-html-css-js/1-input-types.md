# Input types

You already learned about the input HTML tag and how the type property determines the data your users can type in. This cheat sheet should be a reference to decide what type best suits your use case. Most of the inputs go hand in hand with the label tag for best accessibility practices.

## Button

This displays a clickable button and it’s mostly used in HTML forms to activate a script when clicked.

```html
<input type ="button"  value="Click me"  onclick="msg()" />
```

Keep in mind, you can also define buttons with the <button> tag, with the added benefit of being able to place content like text or images inside the tag.

```html
<button onclick="alert('Are you sure you want to continue?')">
  <img
    src="https://yourserver.com/button_img.jpg"
    alt="Submit the form"
    height="64"
    width="64"
  />
   
</button>
```

## Checkbox

Defines a check box allowing single values to be selected or deselected. They are used to let a user select one or more options from a limited number of choices.

```html
<input type="checkbox" id="dog" name="dog" value="Dog">
<label for="dog">I like dogs</label>
<input type="checkbox" id="cat" name="cat" value="Cat">
<label for="cat">I like cats</label>
```

## Radio

Displays a radio button, allowing only a single value to be selected out of multiple choices. They are normally presented in radio groups, which are collections of radio buttons describing a set of related options that share the same name attribute.

```html
<input type="radio" id="light" name="theme" value="Light">
<label for="light">Light</label>
<input type="radio" id="dark" name="theme" value="Dark">
<label for="dark">Dark</label>
```

## Submit

Displays a submit button for submitting all values from an HTML form to a form-handler, typically a server. The form-handler is specified in the form’s action attribute.

```html
<form action="myserver.com" method="POST">
  …
<input type="submit" value="Submit" />
</form>
```

## Text

Defines a basic single-line text field that a user can enter text into.

```html
<label for="fname">First name:</label>
<input type="text" id="fname" name="fname">
```

## Password

Defines a single-line text field whose value is obscured, suited for sensitive information like passwords.

```html
<label for="pwd">Password:</label>
<input type="password" id="pwd" name="pwd">
```

## Date

Displays a control for entering a date (year, month and day) with no time.

```html
<label for="birthdaytime">Birthday (date and time):</label>
<input type="datetime-local" id="birthdaytime" name="birthdaytime">
```

## Datetime-local

Defines a control for entering a date and time, including the year, month and day, as well as the time in hours and minutes.

```html
<label for="birthdaytime">Birthday (date and time):</label>
<input type="datetime-local" id="birthdaytime" name="birthdaytime">
```

## Email

Defines a field for an email address. It’s similar to plain text input, with the addition that it validates automatically when submitted to the server.

```html
<label for="email">Enter your email:</label>
<input type="email" id="email" name="email">
```

## File

Displays a control that lets the user select and upload a file from their computer. To define the types of files permissible you can use the accept attribute. Also, to enable multiple files to be selected, add the multiple attribute.

```html

<label for="myfile">Select a file:</label>
<input type="file" id="myfile" name="myfile">

```

## Hidden

Defines a control that is not displayed but whose value is still submitted to the server.

```html
<input type ="hidden"  id="custId"  name="custId"  value="3487"></input type>
```

## Image

Defines an image as a graphical submit button. You should use the src attribute to point to the location of your image file.

```html
<input type
  ="image"
  src="submit_img.png"
   alt="Submit"
   width="48"
   height="48"
></input type>
```

## Number

Defines a control for entering a number. You can use attributes to specify restrictions, such as min and max values allowed, number intervals or a default value.

```html
<input type
  ="number"
   id="quantity"
   name="quantity"
   min="1"
   max="5"
></input type>
```

## Range

Displays a range widget for specifying a number between two values. The precise value, however, is not considered important. This is typically represented using a slider or dial control. To define the range of acceptable values, use the min and max properties.

```html
<label for="volume">Volume:</label>
<input type="range" id="volume" name="volume" min="0" max="10">
```

## Reset

Displays a button that resets the contents of the form to their default values.

```html
<input type ="reset"></input type>
```

## Search

Defines a text field for entering a search query. These are functionally identical to text inputs, but may be styled differently depending on the browser.

```html
<label for="gsearch">Search in Google:</label>
<input type="search" id="gsearch" name="gsearch">

```
