students_per_hour_1 = int(input())
students_per_hour_2 = int(input())
students_per_hour_3 = int(input())
students = int(input())

total_per_hour = students_per_hour_1 + students_per_hour_2 + students_per_hour_3
hours = 0

while not students == 0:
    hours += 1
    if hours % 4 == 0:
        hours += 1

    if students < total_per_hour:
        students = 0
    else:
        students -= total_per_hour

print(f"Time needed: {hours}h.")