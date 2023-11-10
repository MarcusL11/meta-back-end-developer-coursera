## Grids and flexbox cheat sheet

### Grids

```html
selector { display: grid; /* or inline-grid */ }
```

selector {
display: grid;
grid-template-rows: none;
grid-template-columns: none;
grid-template-areas: none;
grid-auto-rows: auto;
grid-auto-columns: auto;
grid-auto-flow: row;
column-gap: normal;
row-gap: normal;
}

**Grid properties for container:**

| Property              | Description                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| grid-template-columns | Defines the line names and maintains a constant size of column items. Can accept a range of different measurement sizes. |
| grid-template-rows    | Defines the line names and maintains a constant size of rows. Can accept a range of different measurement sizes.         |
| grid-auto-columns     | Determines the default size for columns that have not been explicitly configured.                                        |
| grid-auto-rows        | Determines the default size for rows that have not been explicitly configured.                                           |
| grid-template         | Allows you to define and maintain named cells on a grid.                                                                 |

**Grid properties for items (child):**

| Property          | Description                                                          |
| ----------------- | -------------------------------------------------------------------- |
| grid-column       | Allows for specifying where on the grid the column is to start.      |
| grid-column-start | Determines the starting column position an item is placed on a grid. |
| grid-column-end   | Determines the end column position an item is placed on a grid.      |
| grid-row          | Allows for specifying where on the grid the row is to start.         |
| grid-row-start    | Determines the starting row position an item is placed on a grid.    |
| grid-row-end      | Determines the end row position an item is placed on a grid.         |

### Flexbox

html
selector {
display: flex | inline-flex
}

**Flexbox properties for container:**

| Property        | Description                                                                                                                                                                           |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| flex-direction  | It is possible to specify the direction your elements will follow.                                                                                                                    |
| flex-wrap       | The standard layout is to plot the elements from left to right in a straight line. The wrap feature allows you to customize this to match the size of the window displaying the page. |
| align-items     | Determines how the flex items are to be positioned on the page.                                                                                                                       |
| justify-content | Justify-content determines the alignment of the flex items.                                                                                                                           |

**Flexbox properties for items (child):**

| Property    | Description                                                                                                                                 |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| flex-grow   | This attribute enables the flex container to grow proportionally to the other containers present.                                           |
| flex-shrink | This allows elements to shrink in relation to items around it.                                                                              |
| flex-basis  | Sets the initial main size of an item. It can be overridden if other stylized elements are configured.                                      |
| order       | The standard positioning of items is by source order, however this feature will enable you to configure where the items appear on the page. |
| align-self  | Determines where on the page the child items will be positioned.                                                                            |
