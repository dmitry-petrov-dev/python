# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников

nr_employee = 0
total_salary = 0
employee_low = []
try:
    for line in open("text_3.txt"):
        line_list = line.split()
        salary = float(line_list[1])
        if salary < 20000.0:
            employee_low.append(line_list[0])
        nr_employee += 1
        total_salary += salary
    print(f"Salary less 20000: {', '.join(employee_low)}")
    print(f"Average salary: {total_salary/nr_employee:.1f}")
except FileNotFoundError:
    print("File is not found")
