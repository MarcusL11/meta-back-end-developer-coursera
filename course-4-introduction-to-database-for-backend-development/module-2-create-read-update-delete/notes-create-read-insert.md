### Database Creation and Deletion in SQL

#### Creating a Database

```sql
CREATE DATABASE `<database_name>`;

DROP DATABASE `<database_name>`;

CREATE TABLE `<table_name>` (
    `<column_name1>` `<data_type>`,
    `<column_name2>` `<data_type>`,
    ...
);
```

- CREATE TABLE - Keyword to create a new table.
- <table_name> - The name of the table to be created.
- <column_name1> - The name of the first column in the table.
- <data_type> - The data type of the first column.
- <column_name2> - The name of the second column in the table.
- <data_type> - The data type of the second column.
- ... - Repeat the <column_name> and <data_type> pairs for each column in the table.
- ; - Semicolon to terminate the statement.

```sql
CREATE TABLE `customers` (
    `customer_name` VARCHAR(255),
    `phone_number` INT
);
```

### Altering Tables in SQL

**Syntax**

```sql
ALTER TABLE table_name
    ADD column_name data_type,
    DROP COLUMN column_name,
    MODIFY COLUMN column_name data_type;
```

```sql
ALTER TABLE students
    ADD COLUMN age INT,
    ADD COLUMN nationality VARCHAR(52),
    ADD COLUMN country VARCHAR(100),
    DROP COLUMN nationality,
    MODIFY COLUMN country VARCHAR(100);
```

**Usage**

To alter a database table, use the `ALTER TABLE` statement. This statement allows you to add, drop, or modify columns in a table.

**Add a column**

To add a new column to a table, use the `ADD` keyword followed by the column name and data type.

**Drop a column**

To drop a column from a table, use the `DROP COLUMN` keyword followed by the column name.

**Modify a column**

To modify a column in a table, use the `MODIFY COLUMN` keyword followed by the column name and new data type.

**Example**

The following example shows how to use the `ALTER TABLE` statement to add, drop, and modify columns in a table:

```sql
ALTER TABLE students
ADD COLUMN age INT,
ADD COLUMN nationality VARCHAR(52),
ADD COLUMN country VARCHAR(100),
DROP COLUMN nationality,
MODIFY COLUMN country VARCHAR(100);
```

This statement will add three new columns to the `students` table: `age`, `nationality`, and `country`. It will also drop the `nationality` column and modify the `country` column to have a data type of `VARCHAR(100)`.

**Notes**

- Before you can alter a table, you must have the `ALTER` privilege on the table.
- You cannot add or drop a column that is referenced by a foreign key constraint.
- You cannot modify a column's data type if the column contains data.

## Insert Statements:

```sql
INSERT INTO table_name (column_name1, column_name2, ...)
VALUES (value1, value2, ...);

INSERT INTO players (ID, Name, Age, Start_date)
VALUES (1, 'Yuval', 25, '2020-10-15');

```

## Multiple rows insertion

```sql
INSERT INTO players (ID, Name, Age, Start_date)
VALUES (1, 'Yuval', 25, '2020-10-15'),
       (2, 'Mark', 27, '2020-10-12'),
       (3, 'Karl', 26, '2020-10-07');

```

## Query all data from a table;

```sql
SELECT * FROM players;

```

- The order of the values in the VALUES clause must match the order of the columns in the INSERT INTO clause.
- Non-numeric values must be enclosed in single quotation marks.
- You can use the CURRENT_DATE() function to insert the current date into a column.

```sql
INSERT INTO players (ID, Name, Age, Start_date)
VALUES (4, 'Alex', 22, CURRENT_DATE());
```

This statement will insert a new row into the players table with the following values:

- ID: 4
- Name: Alex
- Age: 22
  -= Start_date: The current date

## Creating a Database Table with SQL

Important Points to Note

- Give meaningful names to your table and columns.
- Be aware of the different data types supported by your database system.
- Specify the appropriate length for data types where applicable.

## Using the CREATE TABLE Statement

```sql
CREATE TABLE customers (
    CustomerId INT,
    FirstName VARCHAR(40),
    LastName VARCHAR(20),
    Company VARCHAR(80),
    Address VARCHAR(70),
    City VARCHAR(40),
    State VARCHAR(40),
    Country VARCHAR(40),
    PostalCode VARCHAR(10),
    Phone VARCHAR(24),
    Fax VARCHAR(24),
    Email VARCHAR(60),
    SupportRapid INT
);
```

This statement will create a table named customers with the following columns:

- CustomerId: An integer column that stores numeric values.
- FirstName: A string column that stores text values up to 40 characters in length.
- LastName: A string column that stores text values up to 20 characters in length.
- Company: A string column that stores text values up to 80 characters in length.
- Address: A string column that stores text values up to 70 characters in length.
- City: A string column that stores text values up to 40 characters in length.
- State: A string column that stores text values up to 40 characters in length.
- Country: A string column that stores text values up to 40 characters in length.
- PostalCode: A string column that stores text values up to 10 characters in length.
- Phone: A string column that stores text values up to 24 characters in length.
- Fax: A string column that stores text values up to 24 characters in length.
- Email: A string column that stores text values up to 60 characters in length.
- SupportRapid: An integer column that stores numeric values.
