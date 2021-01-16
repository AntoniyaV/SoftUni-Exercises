command = input()
companies = {}

while not command == "End":
    company_name, employee_id = command.split(" -> ")

    if company_name not in companies:
        companies[company_name] = [employee_id]

    else:
        if employee_id not in companies[company_name]:
            companies[company_name].append(employee_id)

    command = input()

sorted_companies = dict(sorted(companies.items(), key=lambda x: x[0]))

for company, employees in sorted_companies.items():
    print(company)

    for employee in employees:
        print(f"-- {employee}")