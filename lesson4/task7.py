# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
# за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def fact(my_num=1):
    factorial = 1
    for i in range(1, my_num + 1):
        factorial *= i
        yield factorial


try:
    n = int(input("Enter number: "))
    if n <= 0:
        raise Exception("Enter number greater or equals 0")
except (ValueError, Exception):
    print("Entered invalid number")

for el in fact(n):
    print(el)
