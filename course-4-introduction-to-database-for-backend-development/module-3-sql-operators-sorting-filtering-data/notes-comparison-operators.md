# SQL comparison operators

- Comparison operators are used to compare two values or expressions in SQL.
- They can be used to filter data and to include and exclude data.
- SQL uses common mathematical comparison operators:
  - Equal to (=)
  - Less than (<)
  - Greater than (>)
  - Less than or equal to (<=)
  - Greater than or equal to (>=)
  - Not equal to (<>)

These operators are commonly used in other programming languages;
| Operator | What it does |
| ---------| -------------|
| = | Check for equlality |
| <> or != | Check for not inequality|
| > | Check it something is greater than |
| >= | Check if something is greater than or equal|
| < | Check if something is less than|
| <= | Checks if soething is less than or equal|

---

**Example:**

```sql
SELECT *
FROM employee
WHERE salary = 18000;
```

This query will return all employees with a salary of $18,000.

Other examples:

- Find all employees with a salary less than $24,000:

```sql
SELECT *
FROM employee
WHERE salary < 24000;
```

Find all employees with a salary greater than or equal to $24,000:

```sql
SELECT *
FROM employee
WHERE salary >= 24000;
```

Find all employees with a salary not equal to $24,000:

```sql
SELECT *
FROM employee
WHERE salary <> 24000;
```

## Exercise:

Retrieve the data for the employee whose ID value is 1, you can use this SELECT statement.

Table name: employee

| employee_ID | employee_name | salary | hours | allowance | tax  |
| ----------- | ------------- | ------ | ----- | --------- | ---- |
| 1           | Alex          | 24000  | 10    | 1000      | 1000 |
| 2           | John          | 55000  | 11    | 3000      | 2000 |
| 3           | James         | 52000  | 7     | 3000      | 2000 |
| 4           | Sam           | 24000  | 11    | 1000      | 1000 |

```sql
SELECT * FROM employee WHERE employee_id = 1;
```

Answer:
| employee_ID | employee_name | salary | hours | allowance | tax |
| ----------- | ------------- | ------ | ----- | --------- | ---- |
| 1 | Alex | 24000 | 10 | 1000 | 1000 |

Now let’s review an example of using the equality operator with a text-based data typed column, the employee_name.

In this example, you need to retrieve the data for the employee whose name is James. You can use the equal operator in the WHERE clause condition.

```sql
SELECT * FROM employee WHERE employee_name = "James";
```

## Inequality comparison operators:

Determine which employee receives a salary that does not equate to 24000. You can use the following SQL statement:

```sql
SELECT * FROM employee where salary != 24000;
```

or

```sql
SELECT * FROM employee where salary <> 24000;
```

The other operators should be common sense based on the examples above.
