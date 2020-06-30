# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv

path, worked_hours, rate, bonus = argv

try:
    worked_hours = float(worked_hours)
    rate = float(rate)
    bonus = float(bonus)
    if worked_hours < 0 or rate <= 0.0 or bonus < 0:
        raise Exception("Entered invalid parameters")
    print("Salary - %.2f" % (worked_hours * rate + bonus))
except (ValueError, Exception):
    print("Entered invalid parameters")
