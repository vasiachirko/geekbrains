class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self, pokritie):
        return self._length * self._width * pokritie.tall * pokritie.mass / 10

class Pokrytie:
    def __init__(self, tall, mass):
        self.mass = mass
        self.tall = tall

print(Road(100, 15).get_mass(Pokrytie(5, 1000)) + 'т')