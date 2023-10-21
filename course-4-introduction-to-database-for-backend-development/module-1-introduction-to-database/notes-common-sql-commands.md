# Common SQL commands

SQL is a language used to interact with databases. It can be used to perform different types of operations in the database, such as creating, inserting, updating, and deleting data.

SQL commands are grouped into four categories:

- **Data Definition Language (DDL)**: DDL commands are used to define the structure of a database, such as creating tables and columns.
- **Data Manipulation Language (DML)**: DML commands are used to manipulate data in a database, such as inserting, updating, and deleting data.
- **Data Control Language (DCL)**: DCL commands are used to control access to a database, such as granting and revoking permissions.
- **Transaction Control Language (TCL)**: TCL commands are used to manage transactions in a database, such as committing and rolling back changes.

Here are some of the most common SQL commands:

## DDL

- **CREATE TABLE:** This command is used to create a new table in a database.
  ```sql
  CREATE TABLE table_name
      (
        column_name1 datatype(size),
        column_name2 datatype(size),
        column_name3 datatype(size)
      );
  ```
- **INSERT INTO:** This command is used to insert new data into a table.

```sql

```

- **ALTER:** This command is used to update existing data in a table.

```sql
ALTER TABLE table_name ADD (column_name datatype(size))
```

- **DROP:** This command is used to delete data from a table.

```sql
DROP TABLE table_name;
```

- **TRUNCATE** This command removes all records but not the table.

```sql
TRUNCATE TABLE table_name;
```

- **COMMENT** This command is to add comments to explain or document SQL statement.

```sql
--Retrieve all data from a table
SELECT * FORM table_name;
```

# DML

- **SELECT** This command retireve data from tables in the database.

```sql
SELECT * FROM table_name;
```

- **INSERT** This command add records of data into an existing table

```sql
INSERT INTO table_name (column1, column2, column3)
    VALUES (value1,value2,value3);
```

- **UPDATE** This command modify or udpdate data contained within a table in the databse

```sql
UPDATE table_name SET column1 = value1, column2 = value1 WHERE condition;
```

- **DELETE** This command delete data from a table in the database

```sql
DELETE FROM table_name WHERE condition;
```

# DCL

- **GRANT** Command to provide users of the database with the priviledges required to allow users to access and manupulate the database
- **REVOKE** Command to remove permission from any users.

# TCL

- **COMMIT** This command will save all work you have already done in the database.
- **ROLLBACK** This command will restore a database to the last comitted state.

These are just some of the most common SQL commands. There are many other commands available, and the specific commands that you need to use will depend on the specific task that you are trying to accomplish.

For more information on SQL commands, please refer to the [SQL documentation](https://www.w3schools.com/sql/).
