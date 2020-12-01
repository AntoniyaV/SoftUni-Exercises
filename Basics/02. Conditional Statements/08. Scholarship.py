income = float(input())
avg_score = float(input())
min_salary = float(input())
import math
social = math.floor(min_salary * 0.35)
excellence = math.floor(avg_score * 25)
if income < min_salary:
    if avg_score >= 5.5:
        if social > excellence:
            print(f"You get a Social scholarship {social} BGN")
        elif social <= excellence:
            print(f"You get a scholarship for excellent results {excellence} BGN")
    elif avg_score > 4.5:
        print(f"You get a Social scholarship {social} BGN")
    else:
        print("You cannot get a scholarship!")
else:
    if avg_score >= 5.5:
        print(f"You get a scholarship for excellent results {excellence} BGN")
    else:
        print("You cannot get a scholarship!")