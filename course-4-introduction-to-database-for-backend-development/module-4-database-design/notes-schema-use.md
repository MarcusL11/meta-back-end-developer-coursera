# Schema Use

## How to Create a Simple Database Schema

By the end of this video, you'll know how to create a simple database schema using SQL. You'll do this by building the schema for a shopping cart database consisting of three tables:

## Customer table

```sql
CREATE TABLE customer (
  customer_id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  address VARCHAR(255) NOT NULL,
  email VARCHAR(100) NOT NULL,
  phone_number VARCHAR(10) NOT NULL
);
```

## Product Table

```sql
CREATE TABLE product (
  product_id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price NUMERIC(8,2) NOT NULL,
  description VARCHAR(255) NOT NULL
);
```

## Cart Order Table

```sql
CREATE TABLE cart_order (
  order_id INT PRIMARY KEY,
  customer_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  order_date DATE NOT NULL,
  status VARCHAR(100) NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
  FOREIGN KEY (product_id) REFERENCES product (product_id)
);

```

## Primary and foreign keys

The `customer_id` and `product_id` fields in the cart_order table are foreign keys that reference the same fields in the customer and product tables, respectively. This establishes a relationship between the three tables, meaning that each order in the `cart_order` table is associated with a specific customer and a specific product.
