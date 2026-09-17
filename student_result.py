import json
import csv
import os

DATA_FILE = "students.json"
CSV_FILE = "student_results.csv"

SUBJECTS = [
    "Python",
    "DBMS",
    "Operating Systems",
    "Software Engineering",
    "Java"
]


def load_students():
    """Load student records from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not load student data.")
        return []


def save_students(students):
    """Save student records to JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(students, file, indent=4)

    except OSError:
        print("Error: Could not save student data.")


def get_valid_marks(subject):
    """Get valid marks between 0 and 100."""
    while True:
        try:
            marks = float(
                input(f"Enter marks in {subject} (0-100): ").strip()
            )

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def calculate_result(marks):
    """Calculate total, percentage, grade and status."""
    total = sum(marks.values())
    percentage = total / len(SUBJECTS)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    status = (
        "PASS"
        if all(mark >= 40 for mark in marks.values())
        else "FAIL"
    )

    return total, percentage, grade, status


def find_student(students, roll_no):
    """Find a student using roll number."""
    for student in students:
        if student["roll_no"].lower() == roll_no.lower():
            return student

    return None


def add_student(students):
    """Add a new student record."""
    print("\n--- Add Student ---")

    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    if not roll_no:
        print("Roll number cannot be empty.")
        return

    if find_student(students, roll_no):
        print("A student with this roll number already exists.")
        return

    marks = {}

    for subject in SUBJECTS:
        marks[subject] = get_valid_marks(subject)

    total, percentage, grade, status = calculate_result(marks)

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status
    }

    students.append(student)
    save_students(students)

    print("\nStudent added successfully.")


def display_student(student):
    """Display complete student result."""
    print("\n" + "=" * 50)
    print("              STUDENT RESULT")
    print("=" * 50)

    print(f"Name        : {student['name']}")
    print(f"Roll Number : {student['roll_no']}")

    print("-" * 50)

    for subject, marks in student["marks"].items():
        print(f"{subject:<28}: {marks:.2f}")

    print("-" * 50)

    print(f"Total       : {student['total']:.2f}")
    print(f"Percentage  : {student['percentage']:.2f}%")
    print(f"Grade       : {student['grade']}")
    print(f"Status      : {student['status']}")

    print("=" * 50)


def view_students(students):
    """Display all student records."""
    if not students:
        print("\nNo student records found.")
        return

    print("\n--- All Students ---")

    for student in students:
        display_student(student)


def search_student(students):
    """Search student by roll number."""
    roll_no = input(
        "\nEnter roll number to search: "
    ).strip()

    student = find_student(students, roll_no)

    if student:
        display_student(student)
    else:
        print("Student not found.")


def update_student(students):
    """Update marks of an existing student."""
    roll_no = input(
        "\nEnter roll number to update: "
    ).strip()

    student = find_student(students, roll_no)

    if not student:
        print("Student not found.")
        return

    print(f"\nUpdating result for: {student['name']}")
    print("Enter new marks:")

    for subject in SUBJECTS:
        student["marks"][subject] = get_valid_marks(subject)

    total, percentage, grade, status = calculate_result(
        student["marks"]
    )

    student["total"] = total
    student["percentage"] = percentage
    student["grade"] = grade
    student["status"] = status

    save_students(students)

    print("Student result updated successfully.")


def delete_student(students):
    """Delete a student after confirmation."""
    roll_no = input(
        "\nEnter roll number to delete: "
    ).strip()

    student = find_student(students, roll_no)

    if not student:
        print("Student not found.")
        return

    print(f"\nStudent: {student['name']}")

    confirm = input(
        "Delete this student? (yes/no): "
    ).strip().lower()

    if confirm == "yes":
        students.remove(student)
        save_students(students)
        print("Student deleted successfully.")
    else:
        print("Delete operation cancelled.")


def class_report(students):
    """Display overall class performance."""
    if not students:
        print("\nNo student records found.")
        return

    total_students = len(students)

    passed = sum(
        1
        for student in students
        if student["status"] == "PASS"
    )

    failed = total_students - passed

    average = (
        sum(student["percentage"] for student in students)
        / total_students
    )

    highest = max(
        students,
        key=lambda student: student["percentage"]
    )

    lowest = min(
        students,
        key=lambda student: student["percentage"]
    )

    print("\n" + "=" * 50)
    print("                 CLASS REPORT")
    print("=" * 50)

    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")
    print(f"Class Average  : {average:.2f}%")

    print(
        f"\nHighest Score  : {highest['name']} - "
        f"{highest['percentage']:.2f}%"
    )

    print(
        f"Lowest Score   : {lowest['name']} - "
        f"{lowest['percentage']:.2f}%"
    )

    print("=" * 50)


def ranking(students):
    """Display students ranked by percentage."""
    if not students:
        print("\nNo student records found.")
        return

    ranked_students = sorted(
        students,
        key=lambda student: student["percentage"],
        reverse=True
    )

    print("\n" + "=" * 60)
    print("                    STUDENT RANKING")
    print("=" * 60)

    for rank, student in enumerate(
        ranked_students,
        start=1
    ):
        print(
            f"{rank}. {student['name']} "
            f"({student['roll_no']}) - "
            f"{student['percentage']:.2f}% - "
            f"{student['grade']}"
        )

    print("=" * 60)


def subject_report(students):
    """Display subject-wise performance."""
    if not students:
        print("\nNo student records found.")
        return

    print("\n--- Subject Wise Report ---")

    for subject in SUBJECTS:
        marks = [
            student["marks"][subject]
            for student in students
        ]

        average = sum(marks) / len(marks)
        highest = max(marks)
        lowest = min(marks)

        print(f"\n{subject}")
        print(f"Average : {average:.2f}")
        print(f"Highest : {highest:.2f}")
        print(f"Lowest  : {lowest:.2f}")


def export_csv(students):
    """Export student results to CSV file."""
    if not students:
        print("\nNo student records to export.")
        return

    try:
        with open(
            CSV_FILE,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            header = (
                ["Name", "Roll Number"]
                + SUBJECTS
                + [
                    "Total",
                    "Percentage",
                    "Grade",
                    "Status"
                ]
            )

            writer.writerow(header)

            for student in students:
                row = [
                    student["name"],
                    student["roll_no"]
                ]

                for subject in SUBJECTS:
                    row.append(
                        student["marks"][subject]
                    )

                row.extend([
                    student["total"],
                    student["percentage"],
                    student["grade"],
                    student["status"]
                ])

                writer.writerow(row)

        print(
            f"\nResults exported successfully to "
            f"{CSV_FILE}"
        )

    except OSError:
        print("Error while exporting CSV file.")


def main():
    """Main program menu."""
    students = load_students()

    while True:
        print("\n" + "=" * 55)
        print("       STUDENT RESULT MANAGEMENT SYSTEM")
        print("=" * 55)

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Class Report")
        print("7. Student Ranking")
        print("8. Subject Wise Report")
        print("9. Export Results to CSV")
        print("10. Exit")

        choice = input(
            "\nEnter your choice (1-10): "
        ).strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            class_report(students)

        elif choice == "7":
            ranking(students)

        elif choice == "8":
            subject_report(students)

        elif choice == "9":
            export_csv(students)

        elif choice == "10":
            print(
                "\nThank you for using "
                "Student Result Management System."
            )
            break

        else:
            print(
                "Invalid choice. "
                "Please enter a number from 1 to 10."
            )


if __name__ == "__main__":
    main()
