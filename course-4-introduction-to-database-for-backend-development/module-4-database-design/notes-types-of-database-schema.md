# Types of database schema

## Different Kinds of Database Schemas

## Logical database schema

A logical database schema is how the data is organized in terms of tables. In other words, it shows what tables should be in a database, and explains how the attributes of different tables are linked together. Creating a logical database schema means illustrating relationships between components of your data. This is also called entity relationship or ER modeling. It specifies what the relationships between entity types are.

## Example of a logical database schema

Here is a simple ER model that shows the logical schema of an ordering application:

```
graph LR
subgraph Order
    A[Order]
    B[Shipment ID]
    C[Courier ID]
    B --> A
    C --> A
end
subgraph Shipment
    D[Shipment]
    E[Order ID]
    D --> E
end
subgraph Courier
    F[Courier]
    G[Shipment ID]
    F --> G
end
```

The ID attribute in each table is the primary key of the respective entities. It provides a unique identifier for each entry, row, or record in the entities. In the order entity, the shipment ID and courier ID are called foreign keys. But in fact, they are also the primary keys of the shipment and courier entities respectively. This creates a relation between these entities and the order table, which in turn has its own ID as its primary key.

## Physical database schema

A physical database schema is how data is stored on disk. In other words, this involves creating the actual structure of your database using code. In MySQL and other relational databases, developers use SQL to create the database tables and the other database objects.

## Example of a physical database schema

Here is an example of a physical schema for an online store database, written in SQL:

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(10) NOT NULL
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(customer_id),
    product_id INT NOT NULL REFERENCES products(product_id),
    quantity INT NOT NULL,
    transaction_date DATETIME NOT NULL
);
```

Database schemas are vital when it comes to the creation of databases and they form the basis of your application. You should now be able to:

Describe how a logical database schema refers to the organization of data in tables, and how an ER model is used to specify relationships between entities.
Explain what a physical database schema is and how it is used to control how data is physically stored on disk.
Create physical database schemas using SQL statements.
