# SQL ORDER BY clause

The SQL ORDER BY clause is used to sort data in a table in either ascending or descending order.

**Syntax:**

```sql
SELECT column_name1, column_name2, ...
FROM table_name
ORDER BY column_name1 [ASC | DESC], column_name2 [ASC | DESC], ...

-- Sort all students by nationality in ascending order.
SELECT ID, first_name, last_name, nationality
FROM student
ORDER BY nationality ASC;

-- Sort all students by nationality in descending order.
SELECT ID, first_name, last_name, nationality
FROM student
ORDER BY nationality DESC;

-- Sort all students by nationality in ascending order and by date of birth in descending order.
SELECT ID, first_name, last_name, date_of_birth, nationality
FROM student
ORDER BY nationality ASC, date_of_birth DESC;
```

- To sort by multiple columns, simply list the column names in the ORDER BY clause, separated by commas.
- By default, the ORDER BY clause sorts data in ascending order. To sort in descending order, use the DESC keyword.
- The type of data in the column affects how it is sorted. Numeric data is sorted numerically, and text data is sorted alphabetically.

The syntax of initiating the order by clause follows this format;

```sql
SELECT *
FROM Employee
ORDER BY <order by column name>;
```

- the `ASC` and `DESC` keywords are the two main types of ordering
- if the order type is not set, the default will be `ASC`
- Its important to consider what is the data type of the column before performing any order task.

It is also possible to perform order and filteres on multiple columns like so:

```sql
SELECT *
FROM invoices
ORDER BY BillingCity ASC, InvoiceDate DESC;
```
