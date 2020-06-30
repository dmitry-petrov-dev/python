# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.


def my_del(var_1, var_2):
    """Return division result of two numbers var_1/var2"""
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        print("ERROR: Division by Zero")


print(f'Division result is {my_del(float(input("Enter first number: ")), float(input("Enter second number: ")))}')
