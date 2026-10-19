
students = [
    {"name": "Aditya", "marks": [85, 90, 78, 88, 92]},
    {"name": "Rahul", "marks": [70, 75, 80, 72, 68]},
    {"name": "Priya", "marks": [95, 92, 96, 90, 94]},
    {"name": "Neha", "marks": [60, 65, 58, 70, 62]},
    {"name": "Aman", "marks": [40, 45, 50, 42, 48]}
]

print("=== STUDENT PERFORMANCE ANALYSIS ===")

highest_average = 0
top_student = ""

for student in students:
    marks = student["marks"]
    total = sum(marks)
    average = total / len(marks)

    if average >= 80:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    print("\nName:", student["name"])
    print("Total Marks:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)

    if average > highest_average:
        highest_average = average
        top_student = student["name"]

print("\nTop Performer:", top_student)
print("Highest Average:", highest_average)
