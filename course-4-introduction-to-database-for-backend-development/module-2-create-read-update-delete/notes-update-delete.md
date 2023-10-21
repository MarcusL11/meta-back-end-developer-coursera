## Updating a table using the UPDATE statement

**Basic syntax:**

```sql
UPDATE table_name
SET column_name = new_value, column_name = new_value...
WHERE condition;
```

Update the `home_address` and `contact_number` columns for the student with the ID of 3.

```sql
UPDATE student
SET home_address = '123 Main Street', contact_number = '123-456-7890'
WHERE ID = 3;
```

Update the `department` column for all engineering students.

```sql
UPDATE student
SET department = 'Engineering'
WHERE department = 'Computer Science';
```

Update the `home_address` and `department` columns for all students in the engineering department.

```sql
UPDATE student
SET home_address = '123 Main Street', department = 'Engineering'
WHERE department = 'Engineering';
```

**Updating multiple rows:**

To update multiple rows at once, you can use the `WHERE` clause to filter the results. For example, the following statement will update the `department` column for all engineering students:

Update the `department` column for all engineering students.

```sql
UPDATE student
SET department = 'Engineering'
WHERE department = 'Computer Science';
```

**Conclusion:**

The UPDATE statement is a powerful tool that can be used to update data in a table. By understanding the syntax and how to use the `WHERE` clause, you can update data efficiently and accurately.

I have also removed the timestamps, as they are not necessary in Markdown.

## Deleting records from a table using the DELETE statement

**Basic syntax:**

```sql
DELETE FROM table_name
WHERE condition;
```

Delete the record for the student with the last name of Miller.

```sql
DELETE FROM student
WHERE last_name = 'Miller';
```

Delete the records for all students in the engineering department.

```sql
DELETE FROM student
WHERE department = 'Engineering';
```

Delete all records from the `student` table.

```sql
DELETE FROM student;
```

**Important:** Be careful when using the `DELETE` statement, as it cannot be undone. It is a good practice to back up your database before running any `DELETE` statements.

**Conclusion:**

The `DELETE` statement is a powerful tool that can be used to remove data from a table. By understanding the syntax and how to use the `WHERE` clause, you can delete data efficiently and accurately.
