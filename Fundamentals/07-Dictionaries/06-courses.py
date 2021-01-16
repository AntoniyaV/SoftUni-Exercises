command = input()
courses = {}

while not command == "end":
    course_name, student_name = command.split(" : ")

    if course_name not in courses:
        courses[course_name] = [student_name]

    else:
        courses[course_name].append(student_name)

    command = input()

ordered_courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))

for course, students in ordered_courses.items():
    print(f"{course}: {len(students)}")

    sorted_students = sorted(students)
    for student in sorted_students:
        print(f"-- {student}")