# All Selectors and Their Specificity

### Specificity Hierarchy

CSS has a set of rules that it uses to ‘score’ or assign a certain weight to selectors and this creates a specificity hierarchy. Based on the weights, there are four categories in this hierarchy:

| Category                                | Weight |
| --------------------------------------- | ------ |
| Inline styles                           | 1000   |
| IDs                                     | 100    |
| Classes, attributes, and pseudo-classes | 10     |
| Elements and pseudo-elements            | 1      |

### Calculating Scores

CSS uses the hierarchical model internally to calculate the specificity of the selectors used on a web page. But often as the size of CSS code increases, developers unavoidably face rule conflicts. In these cases, developers use the specificity hierarchy to calculate the precedence of CSS rules and to control the outcome of their web pages.

Let's explore a practical example of how to determine the score of a few selectors.

| Selector     | Score |
| ------------ | ----- |
| #hello {}    | 0100  |
| div {}       | 0001  |
| div p.foo {} | 0012  |

### Example 1

```html
p {}  div p {} div p.foo {}
```

p#bar => 1 element & 1 ID =>  0 1 0 1 => Score: 101
p.foo => 1 element & 1 class => 0 0 1 1 => Score: 11
p.p.foo => 1 element & 2 class =>  0 0 2 1 => Score: 21

### Key Takeaways

- Specificity is a ranking or score that helps CSS determine the final rule that will be applied to a given element.
- There are four categories in the specificity hierarchy: inline styles, IDs, classes, attributes, and pseudo-classes, and elements and pseudo-elements.
- The score for a selector is calculated by adding up the weights of the categories in the selector.
- In the case of selectors with equal specificity, the latest or last written rule is the one that will be applied.
- CSS specificity calculators can help you determine the styling outcomes of your pages.
