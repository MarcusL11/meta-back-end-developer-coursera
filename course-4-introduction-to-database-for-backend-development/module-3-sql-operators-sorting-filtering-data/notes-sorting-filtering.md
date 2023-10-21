# The SQL WHERE clause

**Purpose:** The WHERE clause is used to filter data in a SQL statement.

**Syntax:**

```sql
SELECT column_name1, column_name2, ...
FROM table_name
WHERE condition;
```

**Condition:** The condition is an expression that is evaluated for each record in the table. If the condition is true, the record is returned. If the condition is false, the record is not returned.

**Operators:** The WHERE clause can use a variety of operators to compare values. Some common operators include:

- Equal to ( = )
- Less than ( < )
- Greater than ( > )
- Less than or equal to ( <= )
- Greater than or equal to ( >= )
- Not equal to ( <> )
- BETWEEN
- LIKE
- IN

**Examples:**

```sql
-- Select all students in the engineering faculty.
SELECT *
FROM student_table
WHERE faculty = 'engineering';

-- Select all students whose date of birth is between 2010-01-01 and 2010-05-30.
SELECT *
FROM student_table
WHERE date_of_birth BETWEEN '2010-01-01' AND '2010-05-30';

-- Select all students whose faculty starts with the letter 'S'.
SELECT *
FROM student_table
WHERE faculty LIKE 'S%';

-- Select all students who are from the USA or the UK.
SELECT *
FROM student_table
WHERE country IN ('USA', 'UK');
```

**The WHERE clause**

The WHERE clause is useful when you want to filter data in a table based on a given condition in the SQL statement. The WHERE clause in SQL is there for the purpose of filtering records and fetching only the necessary records. This can be used in SQL SELECT, UPDATE, and DELETE statements.

The filtering happens based on a condition. The condition can be written using any of the following comparison or logical operators.

**Comparison operators**

| Operator | Description                                                                                                                          |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| =        | Checks if the values of two operands are equal or not. If yes, then condition becomes true.                                          |
| !=       | Checks if the values of two operands are equal or not. If values are not equal, then condition becomes true.                         |
| <>       | Checks if the values of two operands are equal or not. If values are not equal, then condition becomes true.                         |
| >        | Checks if the value of the left operand is greater than the value of the right operand. If yes, then condition becomes true.         |
| <        | Checks if the value of left operand is less than the value of right operand. If yes, then condition becomes true.                    |
| >=       | Checks if the value of the left operand is greater than or equal to the value of right operand. If yes, then condition becomes true. |
| <=       | Check if the value of the left operand is less than or equal to the value of the right operand. If yes then condition becomes true.  |
| !<       | Checks if the value of the left operand is not less than the value of the right operand. If yes, then condition becomes true.        |
| !>       | Checks if the value of the left operand is not greater than the value of the right operand. If yes, then condition becomes true.     |

**Logical operators**

| Operator | Description                                                                                                                                       |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| ALL      | Used to compare a single value to all the values in another value set.                                                                            |
| AND      | Allows for the existence of multiple conditions in an SQL statement's WHERE clause.                                                               |
| ANY      | Used to compare a value to any applicable value in the list as per the condition.                                                                 |
| BETWEEN  | Used to search for values that are within a set of values, given the minimum value and the maximum value.                                         |
| EXISTS   | Used to search for the presence of a row in a specified table that meets a certain criterion.                                                     |
| IN       | Used to compare a value to a list of literal values that have been specified.                                                                     |
| LIKE     | Used to compare a value to similar values using wildcard operators.                                                                               |
| NOT      | Reverses the meaning of the logical operator with which it is used. For example: NOT EXISTS, NOT BETWEEN, NOT IN, etc. This is a negate operator. |
| OR       | Used to combine multiple conditions in an SQL statement's WHERE clause.                                                                           |
| IS NULL  | Used to compare a value with a NULL value.                                                                                                        |
| UNIQUE   | Searches every row of a specified table for uniqueness (no duplicates).                                                                           |

**Examples**

Here are some examples of how to use the WHERE clause to filter data in a table:

```sql
-- Select all students in the engineering faculty.
SELECT *
FROM student_table
WHERE faculty = 'engineering';

-- Select all students whose date of birth is between 2010-01-01 and 2010-05-30.
SELECT *
FROM student_table
WHERE date_of_birth BETWEEN '2010-01-01' AND '2010-05-30';

-- Select all students whose faculty starts with the letter 'S'.
SELECT *
FROM student_table
WHERE faculty LIKE 'S%';

-- Select all students who are from the USA or the UK.
SELECT *
FROM student_table
WHERE country IN ('USA', 'UK');
```

## Using AND condition;

```sql
SELECT column1, column2, columnN
FROM table_name
WHERE [condition1] AND [condition2]...AND [conditionN];
```

Here, we used `N` to represent any sequence number .

## Here is another example of multiple operators and conditions;

```sql
SELECT *
FROM invoices
WHERE Total > 2 AND (BillingCountry = 'USA' OR BillingCountry = 'France');
```

This is considering data that has a total more than 2 and the country of USA or France.
