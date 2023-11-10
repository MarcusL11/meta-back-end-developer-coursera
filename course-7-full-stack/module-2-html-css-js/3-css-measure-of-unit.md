## CSS Units of Measurement

A web page, as you know it, is two-dimensional, meaning it has width and height. This can be expressed in various ways, such as vertical and horizontal, length and breadth, x and y axis, and so on. Another property of a web page is its size, which can be either static or dynamic. As you delve deeper into CSS code, you'll notice that property values can be declared using different units of measurement. Most of these units are used to account for the dynamism and dimensionality of a web page.

### Absolute Units

Absolute units have a fixed size and remain constant across different devices. They are useful for activities like printing a page but less suitable for the wide variety of devices with varying viewport sizes. Absolute units are typically used when the web page's size is known and will remain constant.

| Unit                   | Name                | Comparison               |
| ---------------------- | ------------------- | ------------------------ |
| Q (Quarter-millimeter) | Quarter-millimeters | 1Q = 1/40th of 1cm       |
| mm (Millimeter)        | Millimeters         | 1mm = 1/10th of 1cm      |
| cm (Centimeter)        | Centimeters         | 1cm = 37.8px = 25.2/64in |
| in (Inch)              | Inches              | 1in = 2.54cm = 96px      |
| pc (Pica)              | Picas               | 1pc = 1/6th of 1in       |
| pt (Point)             | Points              | 1pt = 1/72nd of 1in      |
| px (Pixel)             | Pixels              | 1px = 1/96th of 1in      |

Of these, the pixels and centimeters are most frequently used for defining properties.

### Relative Values

Web pages rarely contain only one element. Even containers like flexboxes and grids usually have multiple elements to which rules are applied. Relative values are defined 'in relation' to other elements within the parent element or the viewport (the visible area of the web page). Given the dynamic nature of web pages and the variable size of devices, relative units are often the preferred choice.

| Unit             | Description and relativity                                      |
| ---------------- | --------------------------------------------------------------- |
| em               | Font size of the parent where present.                          |
| ex               | x-co-ordinate or height of the font element.                    |
| ch               | Width of the font character.                                    |
| rem              | Font size of the root element.                                  |
| lh (Line-height) | Value computed for line height of parent element.               |
| rlh              | Value computed for line height of root element which is <html>. |
| vw               | 1% of the viewport width.                                       |
| vh               | 1% of the viewport height.                                      |
| vmin             | 1% of the smaller dimension of viewport.                        |
| vmax             | 1% of the larger dimension of viewport.                         |
| % (Percentage)   | Denotes a percentage value in relation to its parent element.   |

Many of these units are used in terms of the relative size of fonts. Some units are more suitable depending on the relative context. Like when the dimensions of the viewport are important, it's more appropriate to use vw and vh. In a broader context, the relative units you will see most frequently used are percentage, em, vh, vw, and rem.

Much like the absolute and relative units discussed above, certain properties have their own set of acceptable values that need to be taken into account. For example, color-based properties such
