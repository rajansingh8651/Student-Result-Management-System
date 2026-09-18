# Student Result Management System

A Python-based Student Result Management System that allows users to manage student records, calculate results, generate reports, view rankings, and export result data.

## 🚀 Features

* Add new student records
* Store marks for multiple subjects
* Automatically calculate total marks
* Automatically calculate percentage
* Automatic grade calculation
* Automatic Pass/Fail status
* Search student by roll number
* View all students
* Update student marks
* Delete student records
* Class performance report
* Subject-wise performance report
* Student ranking based on percentage
* Generate formatted student result card
* Export results to CSV
* Store student data permanently using JSON
* Input validation and error handling

## 📚 Subjects

The system currently manages marks for:

* Python
* DBMS
* Operating Systems
* Software Engineering
* Java

## 🛠️ Technologies Used

* Python
* JSON
* CSV
* File Handling
* Functions
* Lists
* Dictionaries
* Exception Handling

## 📂 Project Structure

```text
Student-Result-Management-System/
│
├── student_result.py
├── students.json
├── student_results.csv
├── README.md
└── .gitignore
```

## ▶️ How It Works

The application provides a menu-driven interface.

Users can:

1. Add student information and marks.
2. View all student records.
3. Search for a student using the roll number.
4. Update student marks.
5. Delete student records.
6. Generate a class performance report.
7. View subject-wise performance.
8. View student rankings.
9. Generate an individual student result card.
10. Export result data to a CSV file.

Student information is stored in `students.json`, allowing the data to remain available even after the program is closed.

## 📊 Result Calculation

### Total Marks

```text
Total = Sum of marks obtained in all subjects
```

### Percentage

```text
Percentage = Total Marks / Number of Subjects
```

### Pass/Fail Status

A student is marked **PASS** only if they score at least 40 marks in every subject.

If the student scores below 40 in any subject, the status is **FAIL**.

### Grade

The grade is calculated according to the overall percentage.

| Percentage    | Grade |
| ------------- | ----- |
| 90% and above | A+    |
| 80% – 89.99%  | A     |
| 70% – 79.99%  | B     |
| 60% – 69.99%  | C     |
| 50% – 59.99%  | D     |
| Below 50%     | F     |

## 💾 Data Storage

The project uses JSON file handling to store student records.

```text
students.json
```

This allows student data to persist between program executions.

The project also provides CSV export functionality:

```text
student_results.csv
```

The exported CSV file can be opened using spreadsheet applications.

## ✅ Input Validation

The application validates user input for:

* Empty student names
* Empty roll numbers
* Duplicate roll numbers
* Invalid marks
* Marks outside the 0–100 range
* Invalid menu choices

## 📈 Reports

The system provides different reports, including:

### Class Report

Displays:

* Total number of students
* Number of passed students
* Number of failed students
* Class average percentage
* Highest scoring student
* Lowest scoring student

### Student Ranking

Students are ranked based on their percentage, from highest to lowest.

### Subject-wise Report

Displays the following for each subject:

* Average marks
* Highest marks
* Lowest marks

## 📤 CSV Export

The system can export student results into:

```text
student_results.csv
```

The CSV file contains:

* Student Name
* Roll Number
* Python
* DBMS
* Operating Systems
* Software Engineering
* Java
* Total
* Percentage
* Grade
* Status

## 🔮 Future Improvements

Possible future improvements include:

* Graphical User Interface (GUI)
* Login and authentication
* SQLite/MySQL database integration
* Attendance management
* PDF result generation
* Teacher/Admin dashboard
* Web-based version
* Data visualization charts

## 👨‍💻 Author

**Rajan Singh**

BCA Student | Aspiring Software Developer

GitHub:
https://github.com/rajansingh8651

LinkedIn:
https://www.linkedin.com/in/rajansingh8/

## 📌 Project Status

**Completed — Version 1.0**

This project was developed as a practical Python project to improve programming, problem-solving, file handling, data management, and application development skills.
