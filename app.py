students = [
    (101, "Srishti", 97),
    (102, "Shreya", 92),
    (103, "Sanya", 76),
    (104, "Sneha", 84)
]
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"
print("==============================================")
print(" STUDENT MANAGEMENT AND ACADEMIC PERFORMANCE")
print("==============================================")

with open("academic_report.txt", "w") as f:
    f.write("==============================================\n")
    f.write(" STUDENT MANAGEMENT AND ACADEMIC PERFORMANCE\n")
    f.write("==============================================\n\n")
    f.write("ACADEMIC PERFORMANCE REPORT\n")
    f.write("----------------------------\n\n")
    for student_id, name, marks in students:
        grade = calculate_grade(marks)
        f.write("Student ID: " + str(student_id) + "\n")
        f.write("Student Name: " + name + "\n")
        f.write("Marks: " + str(marks) + "\n")
        f.write("Grade: " + grade + "\n")
        f.write("----------------------------\n")
print("Academic performance report generated successfully.")
print("Report file: academic_report.txt")