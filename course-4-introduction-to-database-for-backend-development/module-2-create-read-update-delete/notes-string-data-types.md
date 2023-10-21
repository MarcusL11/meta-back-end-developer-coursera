# String data types

**String datatype in a database**

- String datatype is used to store data that contains a mix of character types, such as alphabet characters, numeric characters, and special characters.
- The most used string datatypes are CHAR and VARCHAR.

**CHAR datatype**

- CHAR datatype is used to hold characters of a fixed length.
- The length of a CHAR column is defined when the table is created and cannot be changed later.
- CHAR datatype is a good choice when you have a predefined size of character that you want to maintain.

**VARCHAR datatype**

- VARCHAR datatype is used to hold characters of a variable length.
- The length of a VARCHAR column can be changed after the table is created.
- VARCHAR datatype is a good choice when you are not sure how many characters might be inserted in the column field.

**Examples of string datatypes**

- TINYTEXT: Used to define columns that require less than 255 characters, like short paragraphs.
- TEXT: Used to define columns of less than 65,000 characters, like an article.
- MEDIUMTEXT: Defined columns of 16.7 million characters. For example, the text of a book.
- LONGTEXT: Stores up to four gigabytes of text data.
