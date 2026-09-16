# Student Result Management System

A Python-based Student Result Management System that allows users to manage student records, calculate results, generate reports, and export result data.

## Features

* Add new student records
* Store marks for multiple subjects
* Automatically calculate total marks
* Automatically calculate percentage
* Automatic grade calculation
* Automatic Pass/Fail status
* Search student by roll number
* View all students
* Update student name and marks
* Delete student records
* Class performance report
* Subject-wise performance report
* Student ranking based on percentage
* Generate formatted student result card
* Export results to CSV
* Store student data permanently using JSON
* Input validation and error handling

## Subjects

The system currently manages marks for:

* Python
* DBMS
* Operating Systems
* Software Engineering
* Java

## Technologies Used

* Python
* JSON
* CSV
* File Handling
* Functions
* Lists
* Dictionaries
* Exception Handling

## Project Structure

```text
Student-Result-Management-System/
│
├── student_result.py
├── students.json
├── student_results.csv
├── README.md
└── .gitignore
```

## How It Works

The application provides a menu-driven interface.

Users can:

1. Add student information and marks.
2. View existing student records.
3. Search for a student using the roll number.
4. Update student information or marks.
5. Delete student records.
6. Generate class performance reports.
7. View subject-wise performance.
8. View student rankings.
9. Generate an individual result card.
10. Export result data to a CSV file.

Student information is stored in `students.json`, allowing the data to remain available even after the program is closed.

## Result Calculation

The system calculates:

**Total Marks**

```text
Total = Sum of marks obtained in all subjects
```

**Percentage**

```text
Percentage = Total Marks / Number of Subjects
```

A student is marked **Fail** if they score below 40 in any subject.

Otherwise, the grade is calculated according to the percentage.

| Percentage    | Grade |
| ------------- | ----- |
| 90% and above | A+    |
| 80% – 89.99%  | A     |
| 70% – 79.99%  | B     |
| 60% – 69.99%  | C     |
| 50% – 59.99%  | D     |
| Below 50%     | F     |

## Data Storage

The project uses JSON file handling to store student records.

Example:

```text
students.json
```

This allows student data to persist between program executions.

The project also provides CSV export functionality:

```text
student_results.csv
```

The exported CSV file can be opened using spreadsheet applications.

## Input Validation

The application validates user input for:

* Empty student names
* Empty roll numbers
* Duplicate roll numbers
* Invalid marks
* Marks outside the 0–100 range
* Invalid menu choices

## Future Improvements

Possible future improvements include:

* Graphical User Interface (GUI)
* Login and authentication
* SQLite/MySQL database integration
* Attendance management
* PDF result generation
* Teacher/admin dashboard
* Web-based version
* Data visualization charts

## Author

**Rajan Singh**

BCA Student
Interested in Software Development, Python and Technology

## Project Status

**Completed — Version 1.0**

This project was developed as a practical Python project to improve programming, problem-solving, file handling, data management and application development skills.
