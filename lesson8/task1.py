"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def to_sec(cls, data):
        SEC_IN_DAY = 60 * 60 * 24
        SEC_IN_MONTH = SEC_IN_DAY * 30
        SEC_IN_YEAR = SEC_IN_MONTH * 12

        data_strs = data.split('-')
        day = data_strs[0]
        month = data_strs[1]
        year = data_strs[2]
        return int(day) * SEC_IN_DAY + int(month) * SEC_IN_MONTH + int(year) * SEC_IN_YEAR

    @staticmethod
    def validation(data):
        data_strs = data.split('-')
        day = int(data_strs[0])
        month = int(data_strs[1])
        year = int(data_strs[2])
        if month < 1 or month > 12 or day < 1 or day > 31:
            print('Дата не валидна')
        else:
            print('дата прошла валидацию')


Data.validation('18-05-1997')
print(Data.to_sec('18-05-1997'))
