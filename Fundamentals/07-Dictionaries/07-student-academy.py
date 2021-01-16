n = int(input())
students = {}

for num in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in students:
        students[student_name] = [student_grade]

    else:
        students[student_name].append(student_grade)

students_to_remove = []
for student, grade in students.items():
    avg = sum(grade) / len(grade)

    if avg < 4.50:
        students_to_remove.append(student)

for stu in students_to_remove:
    students.pop(stu)

sorted_students = dict(sorted(students.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True))

for student, grade in sorted_students.items():
    print(f"{student} -> {sum(grade) / len(grade):.2f}")
