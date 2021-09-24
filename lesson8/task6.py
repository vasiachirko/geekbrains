"""
Продолжить работу над вторым заданием. Реализуйте
механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый
тип данных.
"""


class OrgSklad:
    def __init__(self, initial_store=None):
        self.store = initial_store if initial_store is not None else {}

    def append(self, item, quantity):
        assert quantity.isnumeric
        if item is not in self.store:
            self.store[item] = {'store': quantity}
        else:
            if 'store' in self.store[item]:
                self.store[item]['store'] += quantity
            else:
                self.store[item]['store'] = quantity

    def move(self, item, department, quantity):
        if item not in self.store:
            raise ValueError('не такой позиции на складе')
        if self.store[item].get('store', 0) < quantity:
            raise ValueError('на складе не хватает')
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
