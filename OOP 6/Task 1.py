# Задача 1.
#
# Описание: Создайте класс Book, который будет содержать информацию о книге (название, автор, год издания).
# Создайте методы для отображения информации о книге и для изменения года издания.
#
# Условия:
#
#  • Создайте конструктор, который будет принимать название, автора и год.
#  • Добавьте метод get_info(), который будет выводить информацию о книге.
#  • Добавьте метод для изменения года издания.
import math
from abc import abstractmethod


# class Book:
#     def __init__(self, title: str, author: str, age: int):
#         self._change_age = None
#         self._title: str = title
#         self._author: str = author
#         self._age: int = age
#
#     def get_info(self):
#         return f'Название книги: {self._title}\nАвтор: {self._author}\nГод издания: {self._age}'
#
#     def change_age(self, change_age: int):
#         self._change_age: int = change_age
#         self._age = self._change_age
#
#
# a = Book('Война и Мир', 'Лев Николаевич Толстой', 1874)
# print(a.get_info())
# a.change_age(1900)
# print(a.get_info())


# Задача 2: Класс для банковского счета
#
# Описание: Создайте класс BankAccount, который будет моделировать банковский счёт. В классе должны быть методы
# для пополнения счёта, снятия денег и вывода текущего баланса.
#
# Условия:
#
#  • Конструктор должен принимать начальный баланс.
#  • Метод deposit(amount) для пополнения счёта.
#  • Метод withdraw(amount) для снятия средств (не должно быть возможности уйти в минус).
#  • Метод get_balance() для отображения текущего баланса.


# class BankAccount:
#
#     def __init__(self, initial_balance: int):
#         self.__initial_balance: int = initial_balance
#
#     def deposit(self, initial_balance: int):
#         self.__initial_balance += initial_balance
#
#     def withdraw(self, initial_balance: int):
#         if self.__initial_balance - initial_balance >= 0:
#             self.__initial_balance -= initial_balance
#         raise 'Баланс будет отрицательный'
#
#     def get_balance(self):
#         print(self.__initial_balance)
#
#
# a = BankAccount(500)
# a.get_balance()
# a.deposit(300)
# a.get_balance()
# # a.withdraw(200)
# # a.get_balance()


# Задача 3: Наследование
#
# Описание: Создайте класс Person, который будет хранить информацию о человеке (имя и возраст), и класс Student,
# который наследуется от Person. В классе Student должны быть добавлены поля для хранения учебного
# заведения и среднего балла.
#
# Условия:
#
#  • Конструктор класса Person должен принимать имя и возраст.
#  • Конструктор класса Student должен дополнительно принимать учебное заведение и средний балл.
#  • Добавьте методы для отображения информации о студенте.


# class Person:
#     def __init__(self, name: str, age: int):
#         self._name: str = name
#         self._age: int = age
#
#
# class Student(Person):
#
#     def __init__(self, name: str, age: int, institution: str, average_score: int):
#         super().__init__(name, age)
#         self._institution: str = institution
#         self._average_score: int = average_score
#
#     def info(self):
#         print(self)
#
#     def __str__(self) -> str:
#         return (f'Имя - {self._name}\nВозраст - {self._age}\nУчебное заведение - {self._institution}\n'
#                 f'Средний бал - {self._average_score}')
#
#
# a = Student('Иван', 19, 'КТЖТ', 88)
# a.info()


# Задача 4: Полиморфизм
#
# Описание: Создайте классы Rectangle и Circle. Оба класса должны иметь метод get_area(),
# который возвращает площадь фигуры. Реализуйте механизм полиморфизма, который позволяет вызвать метод get_area()
# для объекта любого класса.
# Условия:
#  • Класс Rectangle должен принимать длину и ширину, а класс Circle — радиус.
#  • Метод get_area() должен возвращать площадь фигуры.


# class Figure:
#
#     @abstractmethod
#     def get_area(self) -> int:
#         raise NotImplemented('Требуется переопределить метод get_area')
#
#
# class Rectangle(Figure):
#
#     def __init__(self, length: int, width: int):
#         self._length: int = length
#         self._width: int = width
#
#     def get_area(self):
#         return self._length * self._width
#
#
# class Circle(Figure):
#
#     def __init__(self, radius: int):
#         self._radius: int = radius
#
#     def get_area(self):
#         return math.pi * self._radius ** 2


# Задача 1: Система управления библиотекой
# Описание: Реализуйте систему управления библиотекой. В библиотеке могут быть книги и журналы.
# У каждого предмета есть уникальный ID, название, автор (для книг) или издатель (для журналов), и информация о том,
# доступен ли он для выдачи. Необходимо реализовать возможность добавления, удаления и поиска предметов,
# а также возможность "взять на время" и "вернуть" предмет.
#
# Условия:
# - Создайте класс LibraryItem, который будет базовым для Book и Magazine.
# - В классе LibraryItem должно быть поле для уникального ID, названия и статуса доступности.
# - В классе Book добавьте поле для автора, а в классе Magazine — для издателя.
# - Добавьте методы для поиска предметов по названию или ID, для добавления и удаления предметов.
# - Реализуйте методы для "взять на время" и "вернуть" предмет.


# Задача: Система управления видеотекой
#
# Описание: Разработайте систему управления видеотекой, где можно брать в аренду фильмы.
# В системе есть различные виды контента, такие как фильмы, сериалы и документальные фильмы.
# У каждого контента есть уникальный ID, название, режиссер, длительность и информация о доступности для аренды.
# Пользователи могут брать в аренду контент, а затем возвращать его. Также пользователи могут просматривать историю
# арендованных фильмов и оставлять оценки для контента.


class Management:

    def __init__(self, id: int, name: str, director: str, time: float, availability: bool):
        self.__id: int = id
        self.__name: str = name
        self.__director: str = director
        self.__time: float = time
        self.__availability: bool = availability

    @property
    def id(self):
        return self.__id

    def availability(self):
        return self.__availability


class VideoItem:

    def __init__(self):
        self.__items: list[VideoItem] = []

    def add(self, item: Management):
        self.__items.append(item)
