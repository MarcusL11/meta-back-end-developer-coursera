# Districnt Clause

## What is SELECT DISTINCT statement?

- Returns only distinct (different) values.
- Eliminates duplicates from select query result.
- Gets a unique set of results.

## When to use SELECT DISTINCT statement?

- When you want to eliminate duplicates from a select query result.
- When you want to get a unique set of results.

## How to use SELECT DISTINCT statement?

```sql
SELECT DISTINCT column(s) FROM table;
```

**Examples:**

```sql
-- Return distinct values from the `country` column:
SELECT DISTINCT country FROM students;

-- Return distinct values from the `faculty` and `country` columns:
SELECT DISTINCT faculty, country FROM students;

-- Return distinct values from the `country` column, even if the `faculty` column is null:
SELECT DISTINCT country FROM students WHERE faculty IS NULL;
```

**How the SELECT DISTINCT statement interacts with single columns, multiple columns, and null values?**

- **Single column:** Returns distinct values from the specified column.
- **Multiple columns:** Returns distinct values from the combination of the specified columns.
- **Null values:** Considers null to be a unique value.

**Example:**

```sql
-- Return distinct values from the `faculty` and `country` columns, even if one or both columns are null:
SELECT DISTINCT faculty, country FROM students WHERE faculty IS NULL OR country IS NULL;
```
