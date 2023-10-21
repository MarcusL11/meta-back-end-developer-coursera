# Database Schema in Markdown

**What is a database schema?**

A database schema is a plan for how to organize data in a database. It defines the tables, columns, datatypes, and relationships between the tables.

**Different meanings of schema across different database systems**

- In SQL Server, a database schema is a collection of schema objects, such as tables, columns, relationships, datatypes, and keys.
- In Postgres SQL, a database schema is a namespace with the name database objects, such as views, indexes, and functions.
- An Oracle schema system assigns a single schema to each user.

**Advantages of a database schema**

- Logical groupings for database objects
- Easier access and manipulation of database objects
- Greater database security
- Transfer of ownership of schemas and their objects between users and other schemas

**Example of a database schema**

A music database with data for artists, albums, and genres, all stored in separate tables. These tables can be related to one another through various keys, such as the album ID column in the albums table and the artist ID column in the artists table.

## Exploring Database Schema

**What is a database schema?**

A database schema is a plan for how to organize data in a database. It defines the tables, columns, datatypes, and relationships between the tables.

**Three main types of database schema**

- **Conceptual or logical schema:** Defines entities, attributes, and relationships.
- **Internal or physical schema:** Defines how data is stored in secondary storage.
- **External or view schema:** Defines different user views.

**Conceptual or logical schema**

The conceptual or logical schema describes the structure of the entire database for all users. It describes the structure in terms of entities and features of the entities and the relationships between them. An Entity Relationship Diagram (ER-D) is usually drawn to represent the logical schema of a database. At this level, details about the physical storage and retrieval of data are hidden, and the database structure is described only at a concept level. The software developers work with the database at this level.

**Example of a logical schema**

This depicts the employee and department entities in the database along with their attributes and how these two entities are related to each other. This is just a simple example and there’ll be more entities in a real database.

| Entity       | Attribute                              |
| ------------ | -------------------------------------- |
| Employee     | Employee ID, Name, Department ID       |
| Department   | Department ID, Name                    |
| Relationship | One employee belongs to one department |

## Internal or physical schema

The internal or physical schema describes the physical storage of the database. It represents the entire database but at a very low level. This means it describes how the data is really stored on disk in the form of tables, columns, and records. It defines what data is stored in the database and how.

## Example of an internal/physical schema

This example depicts how the employee table should physically store its data. A real database would have more tables and the internal schema would describe the physical representation of all those tables in the entire database.

| Table    | Column        | Datatype     |
| -------- | ------------- | ------------ |
| Employee | Employee ID   | INT          |
| Employee | Name          | VARCHAR(255) |
| Employee | Department ID | INT          |
