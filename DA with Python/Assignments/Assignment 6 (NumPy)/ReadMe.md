# Assignment 06: Learn and Apply NumPy

## Student & Institute Information

* **Institute:** **SMIT**
* Faculty: **Sir Ayan Hussain**
* **Course:** _Data Analytics using Python_

---

### About Assignment

This assignment introduces NumPy as a foundation for numerical computing in Python. It focuses on creating arrays, understanding their dimensions and shapes, selecting and transforming data, and applying calculations to entire arrays. The examples use small, visible datasets so that each operation's result can be inspected directly.

### Learning Goals

By completing the exercises in [Assignment 06 (NumPy).ipynb](Assignment%2006%20(NumPy).ipynb), you practice how to:

* Create one- and multi-dimensional arrays with NumPy constructors.
* Inspect array metadata such as `shape`, `dtype`, and `ndim`.
* Reshape arrays while preserving their values.
* Select elements, rows, columns, and sub-arrays with slicing and indexing.
* Perform elementwise arithmetic, dot products, and aggregate calculations.
* Filter values with Boolean masks and replace values conditionally with `np.where`.
* Combine, sort, and flatten arrays.

### What the Exercises Cover

| Exercises | Concepts |
| --- | --- |
| 1 | Integer ranges with `np.arange`; shape, data type, and dimensions |
| 2 | `np.zeros`, `np.ones`, `np.eye`, and evenly spaced values with `np.linspace` |
| 3 | Reshaping a 1D array into 2D and 3D arrays |
| 4-5 | 1D slicing and 2D row, column, and submatrix indexing |
| 6 | Elementwise arithmetic, exponentiation, and `np.dot` |
| 7 | Sum, mean, minimum, maximum, standard deviation, and axis-based reductions |
| 8 | Reproducible random integers and Boolean-mask filtering/counting |
| 9 | Conditional replacement with `np.where`; locating extrema with `argmax` and `argmin` |
| 10 | Vertical and horizontal stacking, row-wise sorting, and flattening |

### NumPy Patterns to Remember

```python
import numpy as np

values = np.arange(1, 13)
matrix = values.reshape(3, 4)

first_row = matrix[0, :]
third_column = matrix[:, 2]
large_values = matrix[matrix > 6]
row_totals = matrix.sum(axis=1)
column_totals = matrix.sum(axis=0)
```

* In a 2D array, `array[row, column]` selects by position; indices start at `0`.
* A slice's stop index is excluded, so `array[1:4, 1:4]` selects a 3-by-3 region.
* For a 2D array, `axis=1` reduces across columns to produce one result per row; `axis=0` reduces across rows to produce one result per column.
* NumPy arithmetic is elementwise when array shapes are compatible. `np.dot(a, b)` calculates the dot product of two 1D arrays.
* Boolean indexing keeps elements whose condition is `True`. `np.count_nonzero(condition)` counts matches.
* `np.random.default_rng(seed)` provides a random number generator whose results can be reproduced with the same seed.

### Running the Notebook

Run the notebook cells from top to bottom. The first exercise imports NumPy as `np`, and the remaining exercises use that import. The random-number exercise uses a fixed seed (`42`) so its sample and filtered results stay consistent between runs.
& Institute.

### Student Information

* **Student Name:** Muhammad Sarosh Faheem
* **Student ID (STID):** 887187
