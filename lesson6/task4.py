# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
# вызов методов и также покажите результат.


class Car:
    __direction = ["forward", "right", "back", "left"]

    def __init__(self, name, color, speed=0, is_police=False):
        self._name = name
        self._color = color
        self._speed = speed
        self._is_police = is_police

    def go(self, speed):
        self._speed = speed
        print(f"{self._name} {self._color} goes {self._speed}")

    def stop(self):
        self._speed = 0
        print(f"{self._name} {self._color} stops")

    def turn(self, direction="forward"):
        if direction not in self.__direction:
            print(f"Wrong direction, please choice direction from {self.__direction}")
        print(f"Go {direction}")

    def show_speed(self):
        print(f"{self._name} {self._color} speed: {self._speed} km/h")


class TownCar(Car):
    __max_speed = 60

    def __init__(self, name, color, speed=0):
        super().__init__(name, color, speed)

    def show_speed(self):
        print(
            f"Over speed. Max speed - {self.__max_speed} km/h") if self._speed > self.__max_speed else print(
            f"Speed {self._speed} km/h")


class SportCar(Car):
    def __init__(self, name, color, speed=0):
        super().__init__(name, color, speed)


class WorkCar(Car):
    __max_speed = 40

    def __init__(self, name, color, speed=0):
        super().__init__(name, color, speed)

    def show_speed(self):
        print(
            f"Over speed. Max speed - {self.__max_speed} km/h") if self._speed > self.__max_speed else print(
            f"Speed {self._speed} km/h")


class PoliceCar(Car):

    def __init__(self, name, color, speed=0):
        super().__init__(name, color, speed, is_police=True)


town_car1 = TownCar("Skoda", "Blue")
town_car1.go(30)
town_car1.turn("left")
town_car1.show_speed()
town_car1.go(70)
town_car1.show_speed()
town_car1.go(50)
town_car1.stop()
town_car1.show_speed()
print(f"Car color: {town_car1._color}")
print(f"Police car: {town_car1._is_police}")
print()
sport_car1 = SportCar("Ferrari", "Red")
sport_car1.go(200)
sport_car1.turn("forward")
sport_car1.go(150)
sport_car1.turn("left")
sport_car1.go(60)
sport_car1.show_speed()
sport_car1.stop()
print(f"Police car: {sport_car1._is_police}")
print()
work_car1 = WorkCar("Bruder", "Green")
work_car1.go(30)
work_car1.turn("back")
work_car1.turn("right")
work_car1.turn("forward")
work_car1.show_speed()
work_car1.go(50)
work_car1.show_speed()
work_car1.stop()
work_car1.show_speed()
print(f"Police car: {work_car1._is_police}")
print()
police_car1 = PoliceCar("BMW", "White")
police_car1.go(100)
police_car1.turn("forward")
police_car1.go(50)
police_car1.turn("left")
police_car1.go(60)
police_car1.show_speed()
police_car1.stop()
print(f"Police car: {police_car1._is_police}")
