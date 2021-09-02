class Employee:
    name = ''
    salary = 0

    def __init__(self, name, salary = 70000):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'{self.name} ({self.salary})'

    def raise_salary(self, amount):
        self.salary += amount

class Manager(Employee):

    def __str__(self):
        return f'!{self.name} ({self.salary}) подчинённых {len(self.subordinates)}'
    subordinates = []

employee = Employee('Иванов', 100000)
employee2 = Employee('Сидоров', 200000)
employees = [
    employee,
    employee2
]
def average_salary(employees):
    return sum([x.salary for x in employees])/len(employees)

print(average_salary(employees))

manager = Manager("Босс", 500000)
manager.subordinates = [employee, employee2]
[x.raise_salary(10000) for x in manager.subordinates]
print(employee)
print(manager)