judges_num = int(input())
presentation_name = input()

total_grade = 0
grades_num = 0

while presentation_name != "Finish":
    total_grade_presentation = 0
    avg_grade_presentation = 0

    for i in range(judges_num):
        grade = float(input())
        total_grade_presentation += grade
        grades_num += 1

    avg_grade_presentation = total_grade_presentation / judges_num
    print(f"{presentation_name} - {avg_grade_presentation:.2f}.")

    total_grade += total_grade_presentation
    presentation_name = input()

avg_grade = total_grade / grades_num
print(f"Student's final assessment is {avg_grade:.2f}.")