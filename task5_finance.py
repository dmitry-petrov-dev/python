nr_employee = 0
revenue = int(input("Enter company revenue: "))
expense = int(input("Enter company expense: "))
while revenue < 0 or expense < 0:
    if revenue < 0:
        revenue = int(input("Value is not valid. Please enter no negative revenue value: "))
    if expense < 0:
        expense = int(input("Value is not valid. Please enter no negative expense value: "))
if revenue == expense:
    print("Revenue and Expense are equal")
elif revenue > expense:
    print("Profit - ", revenue - expense)
    print("Profitability - ", (revenue - expense) / revenue)
    nr_employee = int(input("Enter number of employee: "))
    while nr_employee <= 0:
        nr_employee = int(input("Invalid value, please enter positive number of employee: "))
    print("Profitability by an employee - ", (revenue - expense) / nr_employee)
else:
    print("Loss - ", expense - revenue)
