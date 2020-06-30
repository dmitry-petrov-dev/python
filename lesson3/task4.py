# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.


def my_func(var_x, var_y):
    """ The function returns result of X ** Y, where X is positive and Y is negative integer """
    if var_x <= 0:
        print("X is not positive float number - ", var_x)
        return
    if var_y >= 0:
        print("Y is not negative number - ", var_y)
        return

    # Option1 with for
    result_1 = 1
    var_x = 1 / var_x
    for i in range(abs(var_y)):
        result_1 *= var_x
    # Option2 with lambda
    result_2 = lambda x1, y1: x1 ** y1

    return result_1, result_2(x, y)


try:
    x = float(input("Input positive number 1: "))
    y = int(input("Input negative number 2: "))
    print(" X to the extent Y is ", my_func(x, y))
except ValueError:
    print("Entered invalid values")
