# Python OOP – School People Management System

## Scenario

A school wants a small Python program to manage its people. Everyone in the school is a `Person`, but students, teachers, and admin staff each have their own details and behavior.

---

### Part 1: Base Class

Create a class `Person` with:

- Attributes: `name`, `age`, `cnic`
- Method `display_info()` that prints name, age, and CNIC
- Method `role()` that returns `"Person"`

### Part 2: Child Classes

Create three classes that inherit from `Person`. Use `super()` in every constructor.

#### Student

Extra attributes:

- `roll_no`
- `marks` (a list of numbers)

Methods:

- `average()` returns the average of marks
- `grade()` returns:
  - `A` for 80+
  - `B` for 70–79
  - `C` for 60–69
  - `F` for below 60
- Override `role()` to return `"Student"`

#### Teacher

Extra attributes:

- `subject`
- `salary`

Methods:

- `annual_salary()` returns `salary × 12`
- Override `role()` to return `"Teacher"`

#### Admin

Extra attributes:

- `department`
- `salary`

Methods:

- `annual_salary()` returns `salary × 12` plus a 10% bonus
- Override `role()` to return `"Admin"`

Each child class must override `display_info()`, call `super().display_info()` first, then print its own extra details.

### Part 3: Polymorphism

Create a list with at least:

- 2 students
- 2 teachers
- 1 admin

Loop through the list and call `role()` and `display_info()` on each object.

Print a line of dashes between each person.

### Part 4: Reports

Using `isinstance()`, write code that:

1. Counts how many students, teachers, and admins there are.
2. Prints the name of the student with the highest average.
3. Prints the total annual salary paid to all staff (teachers and admins).

## OOP Concepts Used

| OOP Concept | Where It Is Used |
|---|---|
| Class | `Person`, `Student`, `Teacher`, `Admin` |
| Object | Objects created from each class |
| Inheritance | `Student`, `Teacher`, and `Admin` inherit from `Person` |
| `super()` | Child constructors and `display_info()` methods |
| Method Overriding | `role()` and `display_info()` |
| Polymorphism | Looping through the `people` list |
| `isinstance()` | Counting and identifying object types |
| Encapsulation | Data and behavior grouped inside classes |

## Notes

- The second teacher has a monthly salary of `100000` so that the total staff salary matches the provided sample total of `3192000`.
- The Admin receives a 10% annual bonus in addition to 12 months of salary.
- The student's grade is calculated from the average of the marks.
