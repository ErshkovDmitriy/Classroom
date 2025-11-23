# class Human:
#
#     def __init__(self, name: str, age: int):
#         self._name: str = Human._validate_name(name)
#         self._age: int = Human._validate_age(age)
#
#     @staticmethod
#     def _validate_name(name: str) -> str:
#         if name.isalpha():
#             return name
#         raise Exception('Имя должно содержать только буквы.')
#
#     @staticmethod
#     def _validate_age(age: int) -> int:
#         if 0 < age < 180:
#             return age
#         raise Exception('Возраст должен быть от 1 до 180.')
#
#     def __str__(self):
#         return f'{self._name} ({self._age})'
#
#
# class Builder(Human):
#
#     def __init__(self, name: str, age: int, work_type: str):
#         super().__init__(name, age)
#         self.__work_type: str = work_type
#
#
# class Pilot(Human):
#
#     def __init__(self, name: str, age: int, health: int):
#         super().__init__(name, age)
#         self.__health = health
#
#     def is_health(self) -> bool:
#         if self.__health < 10:
#             return False
#         return True
#
#
# class Sailor(Human):
#
#     def __init__(self, name: str, age: int, favorite_drink: str):
#         super().__init__(name, age)
#         self.__favorite_drink: str = favorite_drink
#
#     def __str__(self) -> str:
#         return f'Имя: {self._name} \nГода: ({self._age}) \nЛюбимый напиток: {self.__favorite_drink}'
#
#
# s1 = Sailor('andrey', 20, 'Vodka')
# print(s1)


class Passport:

    def __init__(self, name: str, surname: str, patronymic: str, date_of_birth: str):
        self._name: str = name
        self._surname: str = surname
        self._patronymic: str = patronymic
        self._date_of_birth: str = date_of_birth

    def __str__(self) -> str:
        return (f'Имя: {self._name} \nФамилия: {self._surname} \nОтчество: {self._patronymic} \n'
                f'Дата рождения: {self._date_of_birth}')


q1 = Passport('Дмитрий', 'Ершков', 'Владимирович', '10.05.1992')
print(q1)
