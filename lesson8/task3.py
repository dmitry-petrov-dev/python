# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.


list_number = []


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


def is_digit(string):
    """ Function checks input is int or float"""
    if string.isdigit():
        return True
    elif type(string) == float:
        return True
    return False


def convert_numbers(numbers):
    global list_number
    try:
        for num in numbers:
            # Check number is int or float
            if is_digit(num):
                list_number.append(float(num))
            elif num.upper() == 'Q':
                return False
            else:
                raise MyError("You entered not a number!")
    except MyError as error:
        print(error)
    return True


while True:
    my_numbers = input("Enter numbers separated by space or press Q for quit ").split()
    if convert_numbers(my_numbers):
        print("Result is ", list_number)
    else:
        print("Final result is ", list_number)
        break
