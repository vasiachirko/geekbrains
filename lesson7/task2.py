from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def __init__(self, name):
        self.name = name


class Coat(Clothes):

    def __init__(self, name, V):
        self.name = name
        self.V = V

    @property
    def expence_fabric(self):
        return self.V / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name, H):
        self.name = name
        self.H = H

    @property
    def expence_fabric(self):
        return self.H * 2 + 0.3


coat = Coat('Mr.C', 48)
suit = Suit('Jevanchi', 1.8)

print(f'{suit.expence_fabric + coat.expence_fabric:.2f}')
