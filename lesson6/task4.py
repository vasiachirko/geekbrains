from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    speed = 40

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    __directions = ['Вперед', "Вправо", "Назад", "Влево"]
    direction = "Вперед"

    def turn(self, direction):
        res_index = self.__directions.index(self.direction) + direction
        res_index = res_index + 4 if res_index < 0 else res_index
        res_index = res_index - len(self.__directions) if res_index > len(self.__directions) - 1 else res_index
        self.direction = self.__directions[res_index]

    @abstractmethod
    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    
    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('Превышаете')


class WorkCar(Car):
    
    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('Превышаете')


work_car = WorkCar(40, 'yellow with blue', 'Mack', False)
town_car = TownCar(85, 'red', 'Olly', True)
town_car.show_speed()
# work_car.show_speed()
# town_car.show_speed()

town_car.turn(-1)
print(town_car.direction)
town_car.turn(1)
town_car.turn(1)
town_car.turn(1)
town_car.turn(1)
town_car.turn(1)
town_car.turn(1)
print(town_car.direction)
