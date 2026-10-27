# SQL Joins and Group By — Learning Summary

---

## Institute Details

* **Institute:** SMIT
* **Faculty:** Sir Ayan Hussain
* **Course:** Data Analytics with Python (DAP)

## Student Details

* **Name:** Muhammad Sarosh Faheem
* **STID:** 887187

---

## Overview

Assignment 09 focused on SQL joins, aggregate functions, `GROUP BY`, and `HAVING` using the BikeStores database. These concepts help us combine related data, summarize records, and answer practical business questions.

> **Database note:** The assignment uses Microsoft SQL Server syntax and the BikeStores database, with tables under the `production` and `sales` schemas.

## Learning Outcomes

After completing this assignment, we practised how to:

* Retrieve related information from multiple database tables.
* Use `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL OUTER JOIN`.
* Join three or more tables to create reports.
* Use aggregate functions such as `COUNT()`, `MIN()`, `MAX()`, `AVG()`, and `SUM()`.
* Group records with `GROUP BY` and filter groups with `HAVING`.
* Calculate order-line totals and revenue after discounts.
* Sort query results and limit the number of returned rows.
* Execute SQL Server queries through Python and display results with pandas.

---

## 1. INNER JOIN

An `INNER JOIN` returns only rows with matching values in both joined tables.

### What we learned about INNER JOINs

* Combine products with their corresponding brands.
* Retrieve products, brands, and categories together.
* Join tables through related key columns.

**Key takeaway:** Use `INNER JOIN` when only records with matching relationships should appear.

## 2. Joining Multiple Tables

A query can join more than two tables when the required information is stored in separate related tables.

### What we learned about multiple-table joins

* Combine product, brand, and category details.
* Use multiple `JOIN` clauses.
* Filter the joined results with `WHERE`.

**Key takeaway:** Multiple joins make it possible to build a report using data from several related tables.

## 3. LEFT JOIN and Finding Missing Relationships

A `LEFT JOIN` returns every row from the left table and matching rows from the right table. If there is no match, the right-table columns contain `NULL`.

### What we learned about LEFT JOINs

* List all customers, including customers who have never placed an order.
* Find customers without orders by checking for `NULL`.

**Key takeaway:** A `LEFT JOIN` is useful when every record from the left-hand table must remain in the result.

## 4. RIGHT JOIN and FULL OUTER JOIN

### RIGHT JOIN

A `RIGHT JOIN` returns every row from the right-hand table and any matching rows from the left-hand table. In the assignment, it was used to list every store and its staff members.

### FULL OUTER JOIN

A `FULL OUTER JOIN` returns matching rows and unmatched rows from both tables. Unmatched columns contain `NULL`.

The assignment used it to identify products without a stock record:

**Key takeaway:** Outer joins help retain unmatched records and identify missing relationships. In this example, `s.quantity` is `NULL` because no matching stock row exists.

## 5. Multi-Table Joins and Calculated Columns

The order-detail report joined orders, customers, order items, and products.

### What we learned about calculated join reports

* Join four related tables.
* Combine first and last names using `CONCAT()`.
* Calculate a line total after discount.
* Sort the report by order ID and product name.

### Line Total Formula

Line Total = Quantity × List Price × (1 − Discount)

**Key takeaway:** Joining tables and calculating derived values helps create detailed, informative reports.

## 6. Aggregate Functions

Aggregate functions summarize values across multiple rows.

| Function | Purpose |
| --- | --- |
| `COUNT()` | Counts rows or non-`NULL` values, depending on the expression |
| `MIN()` | Returns the minimum value |
| `MAX()` | Returns the maximum value |
| `AVG()` | Calculates the average |
| `SUM()` | Calculates a total |

### What we learned about aggregate functions

We used these functions to calculate the total number of products, the lowest and highest list prices, and the average list price rounded to two decimal places.

**Key takeaway:** Aggregate functions convert individual records into useful summary figures.

## 7. GROUP BY

`GROUP BY` groups rows that share the same value or combination of values, allowing aggregate functions to calculate a result for each group.

### What we learned about GROUP BY

* Count products in each category.
* Calculate average list prices for each brand and model-year combination.
* Sort grouped results.

**Key takeaway:** `GROUP BY` answers questions such as “How many products are in each category?” and “What is the average price for each brand and model year?”

## 8. Grouping Joined Data for Business Analysis

We applied grouping and aggregate functions to customer orders and store revenue.

### What we learned about grouped business analysis

* Count orders for each customer.
* Retain customers with zero orders using `LEFT JOIN`.
* Calculate total revenue per store.
* Combine joins, grouping, `COUNT()`, `SUM()`, and sorting.

**Revenue = SUM(Quantity × List Price × (1 − Discount))**
`Revenue = SUM(Quantity × List Price × (1 − Discount))`

**Key takeaway:** Grouped queries transform transaction-level data into business summaries, such as orders per customer and revenue per store.

## 9. HAVING vs. WHERE

Both clauses filter query results, but they work at different stages.

| `WHERE` | `HAVING` |
| --- | --- |
| Filters individual rows before grouping and aggregation. | Filters groups after `GROUP BY` and aggregation. |
| Commonly filters ordinary column values. | Commonly filters aggregate results such as `COUNT()` or `SUM()`. |
| Example: `WHERE list_price > 1000` | Example: `HAVING COUNT(*) > 20` |

### What we learned about HAVING vs. WHERE

* Find brands with more than 20 products.
* Find customers who have placed three or more orders.
* Apply aggregate conditions using `HAVING`.

**Key takeaway:** Use `WHERE` to filter rows before grouping and `HAVING` to filter groups based on aggregate results.

## 10. Combined Challenge: Top Five Best-Selling Products

The final question combined joins, filtering, aggregation, grouping, sorting, and a row limit.

### What we learned in the top-five challenge

* Join order items, orders, products, and categories.
* Include completed orders using `WHERE o.order_status = 4`.
* Calculate quantity sold using `SUM(oi.quantity)`.
* Calculate revenue after discounts.
* Group results by product and category.
* Return the top five rows using SQL Server's `TOP (5)`.

Filters the records to the completed-order status specified in the assignment.

```sql
SUM(oi.quantity) AS total_quantity_sold
```

Calculates the total quantity sold for each product.

```sql
SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_revenue
```

Calculates revenue for each product, accounting for discounts.

Returns at most five rows after ordering is applied.

**Key takeaway:** Combining these SQL features helps answer business questions about product sales and revenue.

## 11. Executing SQL Queries with Python

We also prepared a Python script to connect to SQL Server, execute the assignment queries, and display the results.

### What we learned from Python database execution

* Python can connect to a database using a compatible connector.
* `pyodbc` can connect Python to Microsoft SQL Server when an appropriate ODBC driver is installed and configured.
* Python can execute SQL queries and retrieve their results.
* `pandas` can display query results in a readable table.
* Connection settings must match the actual database environment.

**Important:** This example assumes Windows Integrated Authentication and a local SQL Server instance. Adjust the connection string if you use another server or SQL Server authentication. The BikeStores database must exist on the server. Python is being used to execute SQL Server queries; this does not make the database MySQL.

---

## 12. Key Takeaways

After completing Assignment 09, we practised these skills:

1. **Data relationships:** Combine related tables through join conditions.
2. **Join types:** Understand how inner and outer joins handle matching and unmatched rows.
3. **Missing relationships:** Use `LEFT JOIN` with `IS NULL` to find records without a match.
4. **Data summarization:** Use `COUNT()`, `MIN()`, `MAX()`, `AVG()`, and `SUM()`.
5. **Grouping:** Summarize data by category, brand, model year, customer, or store.
6. **Aggregate filtering:** Use `HAVING` to filter grouped results.
7. **Business calculations:** Calculate order-line totals and revenue after discounts.
8. **Sorting and limiting:** Use `ORDER BY` and SQL Server's `TOP (5)`.
9. **Python integration:** Execute SQL Server queries through Python and display results with pandas.
10. **Reporting and analysis:** Transform relational data into summaries that support business analysis.

## Conclusion

Assignment 09 provided practical experience with SQL joins, aggregate functions, grouping, and filtering. These concepts are essential for combining data from relational databases, preparing reports, and answering business questions.

By integrating SQL with Python, we also explored how database queries can be executed programmatically and their results processed for further data analysis.

---

## Institute Information

* **Institute:** SMIT
* **Faculty:** Sir Ayan Hussain
* **Course:** Data Analytics with Python (DAP)

## Student Information

* **Name:** Muhammad Sarosh Faheem
* **STID:** 887187

---
