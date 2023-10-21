# Entities and attributes in relational databases

## What is an entity?

An entity is a real-world object or concept that we want to store data about in a database. Entities can be anything from people and places to products and events.

## What is an attribute?

An attribute is a property or characteristic of an entity. For example, some attributes of the entity `Student` might be `name`, `date_of_birth`, and `grade`.

## Different types of attributes

There are different types of attributes in a relational database system, including:

- **Simple attribute:** An attribute that cannot be divided into smaller parts. For example, the `name` attribute of the `Student` entity is a simple attribute.
- **Composite attribute:** An attribute that can be divided into smaller parts. For example, the `address` attribute of the `Student` entity could be divided into smaller parts such as `street`, `city`, and `state`.
- **Single-valued attribute:** An attribute that can only store one value. For example, the `date_of_birth` attribute of the `Student` entity is a single-valued attribute.
- **Multi-valued attribute:** An attribute that can store multiple values. For example, the `phone_number` attribute of the `Student` entity could store multiple phone numbers for a student. However, it is generally best to avoid multi-valued attributes in relational databases.
- **Derived attribute:** An attribute whose value is derived from other attributes. For example, the `age` attribute of the `Student` entity could be derived from the `date_of_birth` attribute.
- **Key attribute:** An attribute that uniquely identifies an entity. For example, the `student_id` attribute of the `Student` entity is a key attribute.

## Identifying entities and attributes for your database

When designing a database, it is important to identify the entities and attributes that are relevant to your project. You should only capture data that is necessary and useful.

To identify entities, think about the real-world objects or concepts that you need to store data about. For example, if you are designing a database for a school, you might identify the following entities:

- Student
- Teacher
- Course
- Grade

Once you have identified the entities, you can start to identify their attributes. Think about the different properties or characteristics of each entity that you need to store data about. For example, some attributes of the `Student` entity might be:

- Name
- Date of birth
- Grade
- Address
- Phone number

## Conclusion

Entities and attributes are the foundation of relational databases. By understanding these concepts, you can design a database that is efficient and effective.
