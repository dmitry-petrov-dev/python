# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def _get_income(self):
        return self._income["wage"], self._income["bonus"]


class Position(Worker):
    def get_full_name(self):
        print(f"Full name: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Total income: {super()._get_income()[0] + super()._get_income()[1]}")


position1 = Position("Vasya", "Pupkin", "Junior Developer", 50000, 25500)
print(position1.name)
print(position1.surname)
print(position1.position)
position1.get_full_name()
position1.get_total_income()
