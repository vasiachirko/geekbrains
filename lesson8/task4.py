"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class OrgSklad:
    def __init__(self, initial_store=None):
        self.store = initial_store if initial_store is not None else []

    def append(self, item):
        self.store.append(item)

    def remove(self, item):
        self.store.remove(item)


class OrgTech:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Printer(OrgTech):
    def __init__(self, name, cost, max_print_size):
        super().__init__(name, cost)
        self.max_print_size = max_print_size


class Xerox(OrgTech):
    def __init__(self, name, cost, phoneNumber):
        super().__init__(name, cost)
        self.phoneNumber = phoneNumber


class Scanner(OrgTech):
    def __init__(self, name, cost, lumen):
        super().__init__(name, cost)
        self.lumen = lumen

