class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        return Cell(self.num - other.num)

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(round(self.num / other.num))

    def make_order(self, other):
        result = ''
        for i in range(other.num // self.num - 1):
            for j in range(self.num):
                result += '*'
            result += '\n'
        for i in range(a if (a:=other.num  % self.num) != 0 else self.num):
            result += '*'
        return result

A = Cell(7)
B = Cell(5)
D = Cell(2)
C = A * B + D
print(A.make_order(C))
