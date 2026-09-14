# Python Assignments 03 & 04

---

## Student and Institute Information

### Institute Details

* **Course:** Data Analysis using Python
* **Faculty:** Sir Ayan Hussain
* **Institute:** SMIT

### Student Details

* **Student:** Muhammad Sarosh Faheem
* **ST-ID:** 887187
* **From:** Karachi

---

## Lists, Strings, Matrices and Dictionaries Practice

---

## 📘 Assignment 03 — Lists, Strings and Matrices

### Assignment 03 Overview

This assignment focuses on developing practical understanding of fundamental Python programming concepts.

The main concepts covered include:

* Lists
* Strings
* Loops
* Conditional Statements
* List Manipulation
* String Manipulation
* Matrices
* Nested Loops
* User Input

The assignment contains 10 programming exercises designed to improve problem-solving skills and understanding of Python fundamentals.

---

### Q1 — Print Alternate Elements of a List

#### Objective — Assignment 03 Q1

Write a program that accepts a list from the user and prints the alternate elements of the list.

#### Concepts Used — Assignment 03 Q1

* Lists
* User Input
* Loops
* Indexing
* `range()`

---

### Q2 — Reverse a List

#### Objective — Assignment 03 Q2

Write a program that accepts a list from the user and reverses the contents of the list without using the `reverse()` method.

#### Concepts Used — Assignment 03 Q2

* Lists
* Loops
* Indexing
* `range()`
* List Manipulation

---

### Q3 — Find the Largest Number

#### Objective — Assignment 03 Q3

Find and display the largest number from a list without using the built-in `max()` function.

#### Concepts Used — Assignment 03 Q3

* Lists
* Loops
* Conditional Statements
* Variables

---

### Q4 — Rotate Elements of a List

#### Objective — Assignment 03 Q4

Rotate the elements of a list so that each element moves to the next position and the last element moves to the first position.

#### Concepts Used — Assignment 03 Q4

* Lists
* Indexing
* Loops
* List Manipulation

---

### Q5 — Delete a Given Word from a String

#### Objective — Q5

Write a program that accepts a string from the user and asks the user to delete a specific word from the string.

#### Concepts Used — Assignment 03 Q5

* Strings
* User Input
* `split()`
* Loops
* Conditional Statements
* Lists
* `join()`

#### Basic Logic — Assignment 03 Q5

```text
Take Sentence
      ↓
Ask User for Word to Delete
      ↓
Convert Sentence into List of Words
      ↓
Check Each Word
      ↓
Skip the Required Word
      ↓
Store Remaining Words
      ↓
Join Words Back into a String
```

---

### Q6 — Convert Date Format

#### Objective — Q6

Write a program that accepts a date in the following format:

```text
mm/dd/yyyy
```

And displays it in the following format:

```text
March 12, 2021
```

#### Concepts Used — Assignment 03 Q6

* Strings
* `split()`
* Lists
* Indexing
* Type Conversion

---

### Q7 — Capitalize Each Word

#### Objective — Q7

Write a function that accepts a sentence and creates a new string where the first character of each word is capitalized.

#### Example — Matrix Addition

**Input:**

```text
stop and smell the roses.
```

**Output:**

```text
Stop And Smell The Roses.
```

#### Concepts Used — Assignment 03 Q7

* Functions
* Strings
* `split()`
* Loops
* `capitalize()`
* `join()`

---

### Q8 — Find the Sum of Each Row of a Matrix

#### Objective — Q8

Find and display the sum of every row in a matrix of size `m × n`.

#### Example Matrix

```text
2   11   7   12
5    2   9   15
8    8  10   42
```

#### Matrix Representation in Python

```python
matrix = [
    [2, 11, 7, 12],
    [5, 2, 9, 15],
    [8, 8, 10, 42]
]
```

#### Concepts Used — Assignment 03 Q9

* Lists
* Nested Lists
* Matrices
* Nested Loops
* Row and Column Indexing
* User Input

#### Basic Logic — Assignment 03 Q8

```text
Matrix
   ↓
Select First Row
   ↓
Add All Elements
   ↓
Display Row Sum
   ↓
Move to Next Row
   ↓
Repeat Until All Rows Are Completed
```

---

### Q9 — Add Two Matrices

#### Objective — Q9

Write a program to add two matrices of size `n × m`.

#### Important Rule — Matrix Multiplication

Both matrices must have the same dimensions.

```text
Matrix 1 = n × m

Matrix 2 = n × m
```

#### Matrix Addition Formula

```text
Matrix1[i][j]
       +
Matrix2[i][j]
       ↓
Result[i][j]
```

#### Example — Matrix Multiplication

**Matrix 1:**

```text
1   2
3   4
```

**Matrix 2:**

```text
5   6
7   8
```

**Result:**

```text
6    8
10   12
```

#### Concepts Used — Assignment 03 Q10

* Matrices
* Nested Lists
* Nested Loops
* Indexing
* User Input
* Arithmetic Operations

---

### Q10 — Multiply Two Matrices

#### Objective — Q10

Write a program to multiply two matrices.

#### Important Rule

Matrix multiplication is possible only when:

```text
Number of Columns in Matrix 1
                =
Number of Rows in Matrix 2
```

#### Matrix Formula

```text
Matrix 1 (m × n)
        ×
Matrix 2 (n × p)
        ↓
Result (m × p)
```

#### Example

**Matrix 1:**

```text
1   2
3   4
```

**Matrix 2:**

```text
5   6
7   8
```

**Result:**

```text
19   22
43   50
```

#### Basic Logic — Assignment 03 Q10

```text
Select Row from Matrix 1
            ↓
Select Column from Matrix 2
            ↓
Multiply Corresponding Elements
            ↓
Add the Results
            ↓
Store Value in Result Matrix
```

#### Concepts Used

* Matrices
* Nested Lists
* Triple Nested Loops
* Indexing
* Arithmetic Operations
* Conditional Statements

---

## 📗 Assignment 04 — Dictionaries

### Assignment 04 Overview

This assignment focuses on understanding Python dictionaries and their practical applications.

The major concepts include:

* Dictionary Creation
* Adding Values
* Updating Values
* Accessing Dictionary Items
* Loops
* Frequency Counting
* Dictionary Methods
* Searching
* Basic Mini Projects

---

### Q1 — Basic Dictionary Creation

#### Objective — Assignment 04 Q1

Create a dictionary named `student` with the following keys:

* Name
* Age
* Course
* City

Print each value individually.

#### Concepts Used — Assignment 04 Q1

* Dictionaries
* Keys
* Values
* Dictionary Access

---

### Q2 — Adding and Updating Dictionary Values

#### Objective — Assignment 04 Q2

Add a new key-value pair and update an existing value in a dictionary.

#### Example Concept

**Add a New Value:**

```python
dictionary["new_key"] = value
```

**Update an Existing Value:**

```python
dictionary["existing_key"] = new_value
```

#### Concepts Used — Assignment 04 Q2

* Dictionaries
* Adding Values
* Updating Values

---

### Q3 — Loop Through a Dictionary

#### Objective — Assignment 04 Q3

Print the keys and values of a dictionary using a loop.

#### Basic Structure

```python
for key, value in dictionary.items():
    print(key, value)
```

#### Concepts Used — Assignment 04 Q3

* Dictionaries
* Loops
* `.items()`

---

### Q4 — Count Frequency of Numbers

#### Objective — Assignment 04 Q4

Create a dictionary that stores how many times each number appears in a list.

#### Example List

```python
[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
```

#### Expected Frequency

```text
1 → 1 Time
2 → 2 Times
3 → 3 Times
4 → 4 Times
```

#### Concepts Used — Assignment 04 Q4

* Lists
* Dictionaries
* Loops
* Conditional Statements
* Frequency Counting

---

### Q5 — Word Counter

#### Objective — Assignment 04 Q5

Accept a sentence from the user and count how many times each word appears.

#### Basic Logic — Assignment 04 Q5

```text
Take Sentence
      ↓
Split Sentence into Words
      ↓
Check Each Word
      ↓
If Word Already Exists
      ↓
Increase Count
      ↓
Otherwise
      ↓
Create New Dictionary Entry
```

#### Concepts Used — Assignment 04 Q5

* Strings
* Dictionaries
* Lists
* `split()`
* Loops
* Conditional Statements

---

### Q6 — Student Marks and Average

#### Objective — Assignment 04 Q6

Calculate the total and average marks from a dictionary containing subject names and marks.

#### Concepts Used — Assignment 04 Q6

* Dictionaries
* `.values()`
* Loops
* Arithmetic Operations
* `len()`

#### Basic Logic — Assignment 04 Q6

```text
Dictionary of Marks
        ↓
Get All Values
        ↓
Calculate Total
        ↓
Divide by Number of Subjects
        ↓
Calculate Average
```

---

### Q7 — Highest Scoring Student

#### Objective — Assignment 04 Q7

Find the student with the highest marks from a dictionary.

#### Concepts Used — Assignment 04 Q7

* Dictionaries
* Loops
* Conditional Statements
* Variables

#### Basic Logic — Assignment 04 Q7

```text
Start with a Student
        ↓
Compare Marks
        ↓
Check Next Student
        ↓
Find Higher Marks
        ↓
Update Highest Student
        ↓
Display Final Result
```

---

### Q8 — Merge Dictionaries

#### Objective — Assignment 04 Q8

Merge two dictionaries into one dictionary.

#### Concepts Used — Assignment 04 Q8

* Dictionaries
* `update()`

#### Basic Logic

```text
Dictionary 1
       +
Dictionary 2
       ↓
Merged Dictionary
```

---

### Q9 — Mini Project: Contact Book

#### Objective — Assignment 04 Q9

Create a simple contact book that:

1. Stores 3 contacts.
2. Searches for a contact using a name.
3. Displays the phone number if the contact exists.
4. Displays `Contact not found` if the contact does not exist.

#### Basic Logic — Assignment 04 Q9

```text
Create Dictionary
       ↓
Add Contacts
       ↓
Ask User for Name
       ↓
Check Name in Dictionary
       ↓
Contact Found?
     /       \
   Yes        No
   ↓          ↓
Show Phone   Contact Not Found
```

#### Concepts Used — Assignment 04 Q9

* Dictionaries
* User Input
* Conditional Statements
* Searching
* Key-Value Pairs

---

## 🧠 Key Learning Outcomes

After completing both assignments, the following Python concepts should be understood.

### Lists

* Creating Lists
* Accessing List Elements
* List Indexing
* Reversing Lists
* Rotating Lists
* Finding Values
* Looping Through Lists

---

### Strings

* Taking String Input
* Splitting Strings
* Joining Strings
* Deleting Words
* Changing Text Format
* Capitalizing Words
* Date Formatting

---

### Matrices

* Matrix Representation Using Nested Lists
* Rows and Columns
* Matrix Indexing
* Nested Loops
* Row Sum Calculation
* Matrix Addition
* Matrix Multiplication

---

### Dictionaries

* Creating Dictionaries
* Keys and Values
* Adding Dictionary Items
* Updating Dictionary Items
* Looping Through Dictionaries
* Frequency Counting
* Searching Values
* Merging Dictionaries

---

## 🔑 Important Python Functions and Methods

| Function / Method | Purpose                                   |
| ----------------- | ----------------------------------------- |
| `input()`         | Takes input from the user                 |
| `print()`         | Displays output                           |
| `len()`           | Finds the length of a list or dictionary  |
| `range()`         | Generates a sequence of numbers for loops |
| `split()`         | Converts a string into a list             |
| `join()`          | Converts a list into a string             |
| `capitalize()`    | Capitalizes the first letter of a word    |
| `.items()`        | Accesses dictionary keys and values       |
| `.values()`       | Accesses dictionary values                |
| `update()`        | Adds or updates dictionary values         |
| `append()`        | Adds an item to a list                    |

---

## 📌 Overall Understanding

Assignment 03 and Assignment 04 are designed to strengthen fundamental Python programming and problem-solving skills.

### Assignment 03 Focus

```text
Lists
   +
Strings
   +
Matrices
   +
Loops
```

### Assignment 04 Focus

```text
Dictionaries
      +
Loops
      +
Conditional Statements
      +
Problem Solving
```

---

## 🎯 Final Learning Summary

Together, these assignments provide practical experience with important Python data structures and programming logic.

By completing these exercises, I've developed an understanding of how to:

* Accept input from users.
* Store and manipulate data using lists.
* Work with strings and individual words.
* Use loops to process data.
* Apply conditional statements for decision-making.
* Create and manipulate matrices.
* Perform matrix addition and multiplication.
* Create and manage dictionaries.
* Count frequencies of numbers and words.
* Search for information in dictionaries.
* Build small practical programs using Python.

These concepts form an important foundation for progressing toward more advanced Python topics such as functions, object-oriented programming, data analysis, automation, and application development.

---

## Student Information & Institute information

### Insitute Information

* **Course:** Data Analysis using Python
* **Faculty:** Sir Ayan Hussain
* **Institute:** SMIT

### Student Information

* **Student:** Muhammad Sarosh Faheem
* **ST-ID:** 887187
* **From:** Karachi

---
