# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


number_1 = int(input("Enter first number [a]: "))
number_2 = int(input("Enter first number [b]: "))

try:
    if number_2 == 0:
        raise MyError("You cannot delete by zero!")
    print(f"Result of deletion [a] by [b]: {number_1 / number_2:.1f}")
except MyError as error:
    print(error)
