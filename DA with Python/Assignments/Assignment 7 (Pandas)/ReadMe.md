# Assignment 07: Learn and Apply Pandas

## Student & Institute Information

* **Institute:** **SMIT**
* **Faculty:** **Sir Ayan Hussain**
* **Course:** _Data Analytics using Python_

---

### About Assignment

This assignment introduces Pandas for organizing, inspecting, cleaning, and analyzing tabular data in Python. It begins with a DataFrame built from a dictionary and a labeled Series, then applies common operations to employee data. The exercises demonstrate how Pandas makes it possible to select, transform, summarize, and combine data with concise expressions.

### Learning Goals

By completing the exercises in [Assignment 07 (Pandas).ipynb](Assignment%2007%20(Pandas).ipynb), you practice how to:

* Create a DataFrame from a dictionary and inspect its rows, shape, columns, and data types.
* Create a Series with custom index labels and access values by label and position.
* Save tabular data to a CSV file and load it with `pd.read_csv()`.
* Select columns and filter rows with Boolean conditions.
* Use `.loc` for label-based access and `.iloc` for position-based access.
* Add, rename, and remove DataFrame columns while preserving the original data.
* Count missing values, fill numeric gaps with column means, and drop remaining incomplete rows.
* Sort records and find the highest-paid employees.
* Group records and calculate multiple summary statistics with `groupby()` and `agg()`.
* Combine related tables with inner and left joins, concatenate rows, and remove duplicates.

### What the Exercises Cover

| Exercises | Concepts |
| --- | --- |
| 1-2 | DataFrames from dictionaries; Series, custom indices, label and positional access, sum, and mean |
| 3 | Writing and reading a CSV file; `head()`, `tail()`, `info()`, and `describe()` |
| 4-5 | Column selection, Boolean filtering, `.loc`, and `.iloc` |
| 6 | Calculated columns, renaming columns, and dropping columns |
| 7 | Missing-value counts, mean imputation, and dropping rows with remaining missing values |
| 8 | Multi-column sorting and selecting top records with `nlargest()` |
| 9 | Grouped averages, counts, and maximum values using `groupby()` and `agg()` |
| 10 | Inner and left merges, concatenation, and duplicate removal |

### Pandas Patterns to Remember

```python
import pandas as pd

employees = pd.DataFrame({
"Name": ["Aarav", "Diya"],
"Age": [28, 35],
"City": ["Delhi", "Mumbai"],
"Salary": [42000, 55000],
})

name_and_salary = employees[["Name", "Salary"]]
over_30 = employees.loc[employees["Age"] > 30]
fourth_employee = employees.iloc[3]
city_summary = employees.groupby("City")["Salary"].agg(["mean", "count", "max"])
```

* Use `df[columns]` to select columns, and Boolean conditions inside `.loc[...]` to filter rows.
* `.loc` uses index and column labels; `.iloc` uses zero-based integer positions. In label-based slices, the ending label is included; in positional slices, the ending position is excluded.
* DataFrame arithmetic operates column-wise when the values align. For example, `df["Bonus"] = df["Salary"] * 0.10` calculates a 10% bonus per row.
* `isna().sum()` counts missing values by column. Fill numeric columns with their means before using `dropna()` to remove rows that still have missing values.
* `groupby()` creates groups; `agg()` applies one or more summary functions to each group.
* `merge()` combines tables using matching keys, while `concat()` stacks rows. Use `drop_duplicates()` to remove repeated records.

### Running the Notebook

Run the notebook cells from top to bottom. The first exercise imports Pandas as `pd` and creates the employee DataFrame used in later exercises. The CSV exercise writes `employees.csv` in the notebook's working directory before loading it again with `pd.read_csv()`. Make sure Pandas is installed in the Python environment selected for the notebook.

---

### Student Information

* **Student Name:** Muhammad Sarosh Faheem
* **Student ID (STID):** 887187
