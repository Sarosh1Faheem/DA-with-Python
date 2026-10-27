# Assignment 08: SQL Querying, Sorting, and Filtering

---

## Student and Institute Details

### Institute Information

* **Institute Name:** SMIT
* **Faculty:** Sir Ayan Hussain
* **Course:** Data Analytics with Python

### Student Information

* **Name:** Muhammad Sarosh Faheem
* **STID:** 887167

---

## 1. Introduction

In this assignment, we learned the fundamentals of SQL querying, sorting, filtering, and retrieving data from a relational database. We used the **BikeStores database** to practice SQL queries on customer and product records.

The assignment focused on retrieving specific information, organizing query results, limiting the number of returned records, implementing pagination, identifying unique values, and applying logical operators to filter data according to multiple conditions.

These concepts are essential for data analytics because they help us extract relevant information from large datasets and prepare data for further analysis.

## 2. Learning Objectives

After completing this assignment, we learned how to:

* Retrieve specific columns from database tables using `SELECT`.
* Filter records according to specific conditions using `WHERE`.
* Sort query results using `ORDER BY`.
* Retrieve a limited number or percentage of records using `TOP`.
* Implement pagination using `OFFSET` and `FETCH NEXT`.
* Identify unique values using `DISTINCT`.
* Apply logical operators such as `AND` and `OR`.
* Filter records using multiple conditions.
* Count records and calculate the expected number of rows in a percentage-based result.
* Write structured SQL queries to retrieve meaningful information for data analysis.

---

## 3. Concepts Learned

### 3.1 SELECT Statement

The `SELECT` statement is used to retrieve data from a database table.

It allows us to specify which columns we want to display in the query results rather than retrieving every column.

**What We Learned:**

* How to retrieve specific columns from a table.
* How to select only the information required for a particular analysis.
* How to specify the table from which data should be retrieved.

### 3.2 WHERE Clause

The `WHERE` clause is used to filter records based on specified conditions.

It helps us retrieve only those records that satisfy our requirements.

**What We Learned:**

* How to filter customers according to their state.
* How to retrieve customers from California using `state = 'CA'`.
* How to exclude records without a recorded phone number using `IS NOT NULL`.
* How to combine multiple conditions in a query.

**Important Note:** SQL uses `IS NULL` and `IS NOT NULL` to check for missing values represented by `NULL`. We should not use `= NULL` or `!= NULL` for these checks.

### 3.3 ORDER BY Clause

The `ORDER BY` clause sorts query results in ascending or descending order.

* `ASC`: Sorts values in ascending order.
* `DESC`: Sorts values in descending order.

**What We Learned:**

* How to sort product records by model year in descending order.
* How to sort products within the same year by price in ascending order.
* How to sort query results using multiple columns.
* How the order of columns in `ORDER BY` determines the sorting priority.

In this example, `model_year DESC` is the primary sorting condition, while `list_price ASC` is the secondary sorting condition.

### 3.4 TOP N and TOP PERCENT

In Microsoft SQL Server, the `TOP` clause limits the number or percentage of rows returned by a query.

#### A. TOP N

`TOP (N)` retrieves a specified number of rows.

This query retrieves the five most expensive products.

#### B. TOP PERCENT

`TOP (PERCENT)` retrieves a specified percentage of rows from the result set.

**What We Learned:**

* How to limit query results to a specific number of records.
* How to retrieve a percentage of the available records.
* How to use `ORDER BY` to determine which records are included in a limited result.
* How to retrieve the most expensive or cheapest products using sorting and row limits.

**Important Note:** SQL Server rounds the number of rows returned by `TOP (PERCENT)` up to the next whole number. The actual row count depends on the number of records in the table.

For a table containing `N` products, the expected number of rows for the top 5% is:

```text
Expected Rows = CEILING(N × 0.05)
```

The `CEILING()` function rounds a numeric value up to the next integer.

### 3.5 OFFSET and FETCH NEXT

The `OFFSET` and `FETCH NEXT` clauses are used for pagination, which means dividing query results into smaller sections or pages.

Pagination is useful when working with large datasets because it allows users to retrieve records in manageable groups.

**What We Learned:**

* How to divide query results into pages.
* How to skip a specified number of rows.
* How to retrieve a fixed number of rows per page.
* How pagination can make large datasets easier to browse.
* Why a consistent sorting order is important when retrieving different pages.

For reliable pagination, we can use a secondary sorting column such as `product_id` to help maintain a consistent order when multiple products have the same price.

### 3.6 DISTINCT Keyword

The `DISTINCT` keyword eliminates duplicate values from query results.

It is useful when we need to identify unique values in a dataset.

This query returns unique combinations of states and cities.

When multiple columns are used with `DISTINCT`, SQL considers the combination of values across those columns. A city can therefore appear more than once if it belongs to different states.

#### C. Retrieve Unique Model Years

This query returns the distinct model years available in the products table.

To count the number of unique model years, we can use:

**What We Learned:**

* How to remove duplicate values from query results.
* How to identify unique states and cities.
* How to retrieve unique combinations of multiple columns.
* How to count distinct values using `COUNT(DISTINCT column_name)`.
* How to combine `DISTINCT` with `ORDER BY` to organize the results.

### 3.7 Logical Operators: AND and OR

Logical operators allow us to combine multiple conditions when filtering records.

#### A. AND Operator

The `AND` operator returns records only when all specified conditions are satisfied.

This query retrieves products priced between $500 and $1,500, including both boundaries.

#### B. OR Operator

The `OR` operator returns records when at least one of the specified conditions is satisfied.

This query retrieves products from either 2019 or 2020.

#### C. Combining AND and OR

We can combine both operators to filter records using multiple conditions.

This query retrieves products that satisfy both of the following requirements:

1. Their list price is between $500 and $1,500, inclusive.
2. Their model year is either 2019 or 2020.

The results are sorted by list price in ascending order.

**What We Learned:**

* How to apply multiple filtering conditions.
* How `AND` requires all connected conditions to be true.
* How `OR` allows either connected condition to be true.
* How to use `BETWEEN` to filter values within an inclusive range.
* How parentheses control the grouping of logical conditions.
* How to combine filtering and sorting in a single query.

---

## 4. SQL Functions and Clauses Practiced

The following table summarizes the SQL keywords, clauses, and functions covered in this assignment.

| SQL Keyword / Function   | Purpose                                                     |
| ------------------------ | ----------------------------------------------------------- |
| `SELECT`                 | Retrieves specified columns from a table.                   |
| `FROM`                   | Specifies the source table.                                 |
| `WHERE`                  | Filters records according to conditions.                    |
| `IS NOT NULL`            | Excludes records with missing values in a specified column. |
| `ORDER BY`               | Sorts query results.                                        |
| `ASC`                    | Sorts values in ascending order.                            |
| `DESC`                   | Sorts values in descending order.                           |
| `TOP (N)`                | Retrieves a specified number of rows.                       |
| `TOP (PERCENT)`          | Retrieves a specified percentage of rows.                   |
| `OFFSET`                 | Skips a specified number of rows.                           |
| `FETCH NEXT`             | Retrieves a specified number of rows after the offset.      |
| `DISTINCT`               | Eliminates duplicate result values or combinations.         |
| `AND`                    | Requires all connected conditions to be satisfied.          |
| `OR`                     | Requires at least one connected condition to be satisfied.  |
| `BETWEEN`                | Filters values within an inclusive range.                   |
| `COUNT(*)`               | Counts rows in a result set.                                |
| `COUNT(DISTINCT column)` | Counts unique, non-NULL values in a column.                 |
| `CEILING()`              | Rounds a numeric value up to the next integer.              |

---

## 5. Practical Applications in Data Analytics

The concepts covered in this assignment are useful in real-world data analysis.

### Customer Analysis

Using `SELECT` and `WHERE`, analysts can retrieve customer information based on location or the availability of contact details.

### Product Analysis

Using `ORDER BY`, analysts can rank products by price or organize them by model year.

### Pricing Analysis

Using `TOP`, analysts can identify the most expensive products or examine a selected percentage of products based on price.

### Data Presentation

Using `OFFSET` and `FETCH NEXT`, applications can display large product datasets page by page instead of showing every record at once.

### Data Exploration

Using `DISTINCT`, analysts can identify unique locations, categories, model years, or other values in a database.

### Business Reporting

Using `AND`, `OR`, and `BETWEEN`, analysts can extract records that satisfy specific business requirements, such as identifying products within a particular price range and from selected model years.

These techniques provide a foundation for querying structured data before performing further analysis with Python and libraries such as Pandas.

---

## 6. Key Takeaways

Through this assignment, we developed an understanding of how to retrieve, filter, sort, and organize data using SQL.

The most important lessons are:

1. **Data Retrieval:** `SELECT` and `FROM` help us choose the columns and tables required for analysis.
2. **Data Filtering:** `WHERE` helps us retrieve records that satisfy specific conditions.
3. **Data Sorting:** `ORDER BY` organizes records in ascending or descending order, including sorting by multiple columns.
4. **Result Limiting:** `TOP` allows us to retrieve a specified number or percentage of records.
5. **Pagination:** `OFFSET` and `FETCH NEXT` allow us to divide query results into manageable pages.
6. **Duplicate Removal:** `DISTINCT` helps us identify unique values and combinations.
7. **Conditional Logic:** `AND` and `OR` allow us to apply multiple conditions when retrieving data.
8. **Basic Aggregation:** `COUNT` helps us count rows and unique values.
9. **Rounding:** `CEILING()` helps calculate the expected number of rows in percentage-based results.
10. **Analytical Thinking:** Combining SQL clauses allows us to answer practical business questions using structured data.

## 7. Conclusion

This assignment provided practical experience with essential SQL querying techniques using the BikeStores database.

We learned how to retrieve selected columns, filter customer and product records, sort results using multiple columns, limit the number of returned records, implement pagination, identify distinct values, and combine logical operators to satisfy multiple conditions.

These skills are fundamental to data analytics because they enable us to extract meaningful information from relational databases efficiently.

Furthermore, understanding these SQL concepts provides a strong foundation for integrating database queries with Python, using Pandas for data manipulation, and performing more advanced data analysis.

---

## Student and Institute Information

### Institute Details

* **Institute Name:** SMIT
* **Faculty:** Sir Ayan Hussain
* **Course:** Data Analytics with Python

### Student Details

* **Name:** Muhammad Sarosh Faheem
* **STID:** 887167

---
