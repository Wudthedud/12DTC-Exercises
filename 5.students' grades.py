def calculate_grade(mark):
    if mark >= 90:
        return 'A+'
    elif 85 <= mark < 90:
        return 'A'
    elif 80 <= mark < 85:
        return 'A-'
    elif 75 <= mark < 80:
        return 'B+'
    elif 70 <= mark < 75:
        return 'B'
    elif 65 <= mark < 70:
        return 'B-'
    elif 60 <= mark < 65:
        return 'C+'
    elif 55 <= mark < 60:
        return 'C'
    elif 50 <= mark < 55:
        return 'C-'
    elif 40 <= mark < 50:
        return 'D'
    else:
        return 'E'

# Initialize lists
student_data = []

while True:
    student_name = input("Enter student name (or 'X' to exit): ").strip().capitalize()

    if student_name.upper() == "X":
        break

    try:
        exam_mark = float(input("Enter exam mark (between 0 and 100): "))
        if 0 <= exam_mark <= 100:
            grade = calculate_grade(exam_mark)
            student_data.append((student_name, exam_mark, grade))
        else:
            print("Invalid input. Exam mark should be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

total_marks = sum(mark for _, mark, _ in student_data)
num_students = len(student_data)
average_mark = total_marks / num_students if num_students > 0 else 0

best_student_name, best_student_mark, _ = max(student_data, key=lambda x: x[1])

print("\nBest Student:")
print("Name:", best_student_name)
print("Mark:", best_student_mark)
print("\nAverage Mark for All Students:", average_mark)

print("\nIndividual Student Grades:")
for name, mark, grade in student_data:
    print(f"{name}: {mark} - Grade: {grade}")
