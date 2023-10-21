# SQL arithmetic operators

Arithmetic operators are commonly used in computer languages to perform a calculation and return the result. In SQL, you can use arithmetic operators to perform mathematical operations in a database.

The SQL arithmetic operators and their symbols are:

- Plus (+) for addition
- Subtraction (-) and asterisk (\*) for multiplication
- Forward slash (/) for division
- Percentage (%) for modulus, which provides the remainder value of a division calculation

To perform a calculation, an operator takes two operands and returns a result. You can use the select command followed by one operand, the addition operator, and the second operand.

For example, to add two numbers, you would use the following syntax:

```sql
SELECT 10 + 15;
```

This would return the result 25. You can use the same syntax with the other arithmetic operators.

```sql
SELECT 100 - 50; -- Returns 50
SELECT 10 * 5; -- Returns 50
SELECT 100 / 5; -- Returns 20
SELECT 100 % 5; -- Returns 0
```

**Practical applications:**

- You can use arithmetic operators to calculate important things such as salary increases or calculate changes to allowances for all the employees accurately and efficiently.
- You can use an arithmetic operation to calculate how many leave days an employee has left.
- You can compare whether employees are meeting company targets.

**Arithmetic operators**

Arithmetic operators are useful when you want to perform mathematical operations on the data in tables while you retrieve them by writing SQL SELECT queries. In SQL, arithmetic operators are used to perform mathematical operations on data. To be more specific, they're used with numerical data stored in database tables.

Arithmetic operators can be used in the SELECT clause as well as in the WHERE clause in a SQL SELECT statement. When an operator is used in the WHERE clause, it's intended to perform the operations on specific rows only. This is because the WHERE clause in SQL is used to filter out data that a particular SQL statement is working on.

All arithmetic operators are used on numerical operands for performing:

- Addition
- Subtraction
- Multiplication
- Division
- Modulus

**Using the addition operator**

The SQL addition operator performs the mathematical addition operation on numerical data within columns in a table. For example, if you want to add the values of two instances of numerical data from two separate columns in the table, then you need to specify the two columns as the first and second operand. The syntax is as follows:

```sql
SELECT column_name1 + column_name2 FROM table_name;
```

```
employee_ID | employee_name | salary | allowance
---------- | -------------- | ------ | ----------
1          | Alex          | 25000  | 1000
2          | John          | 55000  | 1000
3          | James         | 52000  | 1000
4          | Sam           | 30000  | 1000
```

If you want to know the total salaries of all employees with the basic salary and the allowance added to it then you can use the addition operator. The SQL syntax for the addition operator is as follows:

```sql
SELECT salary + allowance FROM employee;
```

Output:

```sql
Salary + allowance
26000
56000
53000
31000
```

**Using the subtraction operator**

The SQL subtraction operator performs mathematical subtraction on numerical data within columns in a database table. If you want to subtract the values of one numerical column from the values of another numerical column, you must specify both columns as the first and second operand along with the subtraction operator. The syntax is as follows:

```sql
SELECT column_name1 - column_name2 FROM table_name;
```

**Example:**

Here's the employee table once again, but this time with a “Tax” column and several instances of new data:

```
employee_ID | employee_name | salary | allowance | tax
---------- | -------------- | ------ | ---------- | ---
1          | Alex          | 24000  | 1000        | 1000
2          | John          | 55000  | 1000        | 2000
3          | James         | 52000  | 1000        | 2000
4          | Sam           | 24000  | 1000        | 1000
```

Let's say you want to retrieve the salaries of employees after deducting tax. This is the SQL syntax that you can use with the subtraction operator to get these results:

```sql
SELECT salary - tax FROM employee;
```

Output:

```
Salary - tax
23000
53000
50000
23000
```
