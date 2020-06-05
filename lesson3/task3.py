# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.


def my_func(var_1, var_2, var_3):
    """ Returns amount of the greatest two arguments"""
    try:
        var_list = [int(var_1), int(var_2), int(var_3)]
        var_list.sort(reverse=True)
        return var_list[0] + var_list[1]
    except ValueError:
        print("Entered invalid value, awaiting numbers")


v1 = input("Enter arg 1: ")
v2 = input("Enter arg 2: ")
v3 = input("Enter arg 3: ")
print("Amount of the greatest two arguments ", my_func(v1, v2, v3))