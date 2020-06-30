# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.


def user_data(name, surname, year, city, email, tel):
    """ Return list of user data [name, surname, year, city, email, tel]"""
    return name, surname, year, city, email, tel


print(' '.join(user_data(name=input("Enter name: "), surname=input("Enter surname: "), year=input("Enter year: "),
                         city=input("Enter city: "), email=input("Enter email: "), tel=input("Enter tel: "))))
