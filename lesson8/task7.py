# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class Complex:
    def __init__(self, x=0, y=0):
        self.real = x
        self.imag = y

    def __str__(self):
        return f'{self.real}+{self.imag}j' if self.imag > 0 else f'{self.real}{self.imag}j'

    def __add__(self, other):
        """ (x1 + y1 * j) + (x2 + y2 * j) = x1 + x2 + (y1 + y2) * j """
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        """ (x1 + y1 * j) * (x2 + y2 * j) = (x1 * x2 - y1 * y2) + (x1 * y2 + x2 * y1) * j """
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)


c1 = Complex(5, -10)
c2 = Complex(3, 5)
print(c1)
print(c1 + c2)
print(c1 * c2)
