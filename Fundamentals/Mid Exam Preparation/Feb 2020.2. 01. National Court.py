employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
total_people = int(input())

people_per_hour = employee_1 + employee_2 + employee_3
hours = 0

while total_people > 0:
    hours += 1
    if not hours % 4 == 0:
        total_people -= people_per_hour

print(f"Time needed: {hours}h.")