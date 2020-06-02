# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.
months_dict = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
print(months_dict)
month_num = int(input("Enter month number [1..12]: "))
for month, lst_num in months_dict.items():
    if month_num in lst_num:
        print(f'Month number {month_num} is {month}')
        break
