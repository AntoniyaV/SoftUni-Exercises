def get_average(numbers):
    return sum(numbers) / len(numbers)


n = int(input())
students = {}

for _ in range(n):
    student_name, student_grade = input().split()

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(float(student_grade))

for name, grades in students.items():
    print(f"{name} -> {' '.join([f'{grade:.2f}' for grade in grades])} (avg: {get_average(grades):.2f})")