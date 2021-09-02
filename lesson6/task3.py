class Worker:
    def __init__(self, name, surname, income):
        self.name = name
        self.surname = surname
        self.position = self
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return sum(self._income.values())


position = Position('Петя', 'Иванов', {'wage': 100000, 'bonus': 20000})
print(position.get_full_name())
print(position.get_total_income())
