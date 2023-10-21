# Default Values

## Database constraints

- Used to limit the type of data that can be stored in a table.
- Can be column-level or table-level.
- Most used constraints:
  - NOT NULL: Prevents empty value fields.
  - DEFAULT: Assigns default values.

### NOT NULL constraint

- Example: Customer table with customer ID and customer name columns.
- SQL statement:

```sql
CREATE TABLE customer (
    customer_id INT NOT NULL,
    customer_name VARCHAR(255) NOT NULL
);
```

### DEFTAUL constraints:

```sql
CREATE TABLE player (name varchar(50) NOT NULL, city varchar(30) DEFAULT "Barcelona");
```

Database constraints are an important part of database design. They help to ensure the accuracy and reliability of data.

I have also added some additional formatting to make the notes more readable, such as adding headings for the different sections and using code blocks for the SQL statements.
