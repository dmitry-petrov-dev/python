# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
# быть бесконечным. Необходимо предусмотреть условие его завершения.

from lesson4.task6_generator import my_generator
from lesson4.task6_cycle import my_cycle

try:
    start_number = int(input("Enter start number: "))
    len_gen = int(input("Enter length of generation: "))
    len_cycle = int(input("Enter length of cycle: "))
    if len_gen < 0 or len_cycle < 0:
        raise Exception("Entered invalid parameters")
    print("Generator of repeating elements: ", my_cycle(my_generator(start_number, len_gen), len_cycle))
except (ValueError, Exception):
    print("Entered invalid parameters")

