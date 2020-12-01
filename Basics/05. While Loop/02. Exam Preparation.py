bad_grades_num = int(input())

bad_grades_count = 0
total_grade = 0
problems_count = 0
last_problem = ""
has_failed = True

while bad_grades_count < bad_grades_num:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break

    problem_grade = int(input())
    if problem_grade <= 4:
        bad_grades_count += 1

    total_grade += problem_grade
    problems_count += 1
    last_problem = problem_name

average = total_grade / problems_count
if has_failed:
    print(f"You need a break, {bad_grades_num} poor grades.")
else:
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {last_problem}")