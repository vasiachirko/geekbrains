"""
Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение
компании. Для хранения данных о наименовании и количестве
единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
"""

class OrgSklad:
    def __init__(self, initial_store=None):
        self.store = initial_store if initial_store is not None else []

    def append(self, item):
        self.store.append(item)
        item.place = 'store'

    def move(self, item, department):
        self.store.remove(item)
        item.place = department


class OrgTech:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.place = None

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


store = OrgSklad()
item = Scanner('bestScannerEver', 10000, 80)
store.move(item, 'Продажи')
