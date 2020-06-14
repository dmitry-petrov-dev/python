# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.


class Stationery:
    def __init__(self):
        self.title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки Pen: {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки Pencil: {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки Handle: {self.title}")


pen1 = Pen()
pen1.title = "Type by pen"
pen1.draw()

pen2 = Pen()
pen2.title = "Type by pen2"
pen2.draw()

pencil1 = Pencil()
pencil1.title = "Type by pencil"
pencil1.draw()

handle1 = Handle()
handle1.title = "Type by handle"
handle1.draw()
