# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

my_dict = {}
try:
    for line in open("text_6.txt"):
        # searching subject
        subject = ""
        for symbol in line:
            if symbol != ":":
                subject += symbol
            else:
                break
        # collect hours
        num = ""
        total_hours = 0
        for symbol in line:
            if symbol.isdigit():
                num += symbol
            else:
                if num != "":
                    total_hours += int(num)
                    num = ""
        my_dict.update({subject: total_hours})
    print(my_dict)
except FileNotFoundError:
    print("File is not found")
