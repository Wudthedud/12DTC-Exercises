students = []
total_marks = 0
num_students = 0
best_student_name, best_student_mark = "", -1

while (student_name := input("Enter student name (or 'X' to exit): ").upper()) != "X":
    try:
        exam_mark = float(input("Enter exam mark (between 0 and 100): "))
        if 0 <= exam_mark <= 100:
            students.append({"name": student_name, "mark": exam_mark})
            total_marks += exam_mark
            num_students += 1
            if exam_mark > best_student_mark:
                best_student_name, best_student_mark = student_name, exam_mark
        else:
            print("Invalid input. Exam mark should be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

average_mark = total_marks / num_students if num_students > 0 else 0

print("\nBest Student:\nName:", best_student_name, "\nMark:", best_student_mark)
print("\nAverage Mark for All Students:", average_mark)

print("\nUniversity Style Grades:")
for student in students:
    name, mark = student["name"], student["mark"]
    if mark >= 90:
        grade = "A+"
    elif 85 <= mark < 90:
        grade = "A"
    elif 80 <= mark < 85:
        grade = "A-"
    elif 75 <= mark < 80:
        grade = "B+"
    elif 70 <= mark < 75:
        grade = "B"
    elif 65 <= mark < 70:
        grade = "B-"
    elif 60 <= mark < 65:
        grade = "C+"
    elif 55 <= mark < 60:
        grade = "C"
    elif 50 <= mark < 55:
        grade = "C-"
    elif 40 <= mark < 50:
        grade = "D"
    else:
        grade = "E"
    
    print(f"{name}: {grade}")