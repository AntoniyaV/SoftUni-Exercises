tabs = int(input())
salary = int(input())

for site in range(tabs):
    site_name = input()

    if site_name == "Facebook":
        salary -= 150
    elif site_name == "Instagram":
        salary -= 100
    elif site_name == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)