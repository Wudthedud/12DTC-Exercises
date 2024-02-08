total_marks = 0
num_students = 0
best_student_name, best_student_mark = "", -1

while (student_name := input("Enter student name (or 'X' to exit): ").upper()) != "X":
    try:
        exam_mark = float(input("Enter exam mark (between 0 and 100): "))
        if 0 <= exam_mark <= 100:
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
