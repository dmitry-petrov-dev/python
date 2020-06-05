# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.

total = 0


def is_digit(string):
    """ Function checks input is int or float"""
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def calc_sum(numbers):
    """ Function adds numbers in list to total """
    global total
    for num in numbers:
        # Check number is int or float
        if is_digit(num):
            total += float(num)
        elif num.upper() == 'Q':
            return False
        else:
            # Entered something else
            print("You entered incorrect sequence")
            return False
    print("Result is ", total)
    return True


while True:
    my_numbers = input("Enter numbers separated by space or press Q for quit ").split()
    if not calc_sum(my_numbers):
        print("Result is ", total)
        break
