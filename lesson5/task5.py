# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.


from random import randint

amount = 0
list_numbers = [randint(1, 10) for i in range(10)]
with open("text_result_5.txt", "w") as f_obj:
    print(' '.join(map(str, list_numbers)), file=f_obj)
for line in open("text_result_5.txt"):
    for number in line.split():
        amount += int(number)
    print(f"Numbers: {list_numbers}")
    print(f"Amount: {amount}")