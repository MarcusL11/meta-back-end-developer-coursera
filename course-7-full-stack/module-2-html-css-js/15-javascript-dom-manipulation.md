## DOM Manipulation Basics

**What is DOM manipulation?**

DOM manipulation is the process of changing the structure, content, or style of a web page using JavaScript. The DOM (Document Object Model) is a tree-like representation of a web page in JavaScript. By manipulating the DOM, you can dynamically update the web page without reloading it.

**How to manipulate the DOM**

There are two main ways to manipulate the DOM: using the Elements tab in the browser's DevTools, or using JavaScript code.

To manipulate the DOM using the Elements tab:

1. Open the browser's DevTools (usually by pressing `Ctrl`+`Shift`+`I` on Windows or `Cmd`+`Opt`+`I` on Mac).
2. Click on the Elements tab.
3. Select the element you want to manipulate.
4. Use the properties panel to change the element's attributes, styles, or content.

To manipulate the DOM using JavaScript code, you can use the following methods:

- `document.createElement()`: Creates a new HTML element.
- `document.createTextNode()`: Creates a new text node.
- `document.querySelector()`: Selects the first element that matches the specified CSS selector.
- `document.querySelectorAll()`: Selects all elements that match the specified CSS selector.
- `element.appendChild()`: Appends a child element to the specified element.
- `element.removeChild()`: Removes a child element from the specified element.
- `element.setAttribute()`: Sets an attribute on the specified element.
- `element.getAttribute()`: Gets the value of an attribute on the specified element.
- `element.textContent`: Gets or sets the text content of the specified element.

**Example**

The following code demonstrates how to manipulate the DOM to add a heading 2 element to a web page:

```javascript
// Create a new heading 2 element.
const h2 = document.createElement("h2");

// Set the text content of the heading 2 element.
h2.textContent = "This is an h2 heading.";

// Set the ID and class attributes on the heading 2 element.
h2.setAttribute("id", "sub-heading");
h2.setAttribute("class", "secondary");

// Append the heading 2 element to the body of the web page.
document.body.appendChild(h2);
```

**Conclusion**

DOM manipulation is a powerful tool that allows you to dynamically update web pages. By understanding the basics of DOM manipulation, you can write more efficient and effective JavaScript code.
