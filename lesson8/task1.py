# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.str_date = date

    @classmethod
    def convert(cls, date):
        str_date = date.split("-")
        cls.dd = int(str_date[0])
        cls.mm = int(str_date[1])
        cls.yyyy = int(str_date[2])
        return cls.validation(cls.dd, cls.mm, cls.yyyy)

    @staticmethod
    def validation(day, month, year):
        if year < 1 or year > 9999:
            return "Year is not correct"
        if month < 1 or month > 12:
            return "Month is not correct"
        if day < 1 or day > 31:
            return "Day is not correct"
        elif day == 31 and month in [4, 6, 9, 11]:
            return f"In month {month} - 30 days, you entered {day}"
        elif month == 2:
            if (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)) and day > 28:
                return f"In February {year} - 28 days, you entered {day}"
            else:
                if day != 29:
                    return f"In February {year} - 29 days, you entered {day}"
        return day, month, year


print(Date.convert("31-01-2000"))
print(Date.convert("00-01-2000"))
print(Date.convert("30-02-2000"))
print(Date.convert("01-01-0000"))
print(Date.convert("13-13-2013"))
