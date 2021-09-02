from time import sleep
from sys import exit
class TraficLight:
    __color = 'red'
    __flag = True
    __flag_prev_color_green = True

    def running(self):
        if self.__color == 'red':
            sleep(7)
            self.__color = 'yellow'
            if not self.__flag_prev_color_green:
                print('Нельзя так переключать')
                exit(1)
            self.__flag_prev_color_green = False
        elif self.__color == 'yellow':
            if self.__flag:
                self.__flag = False
                self.__color = 'green'
            else:
                self.__flag = True
                self.__color = 'red'
            sleep(2)
        elif self.__color == 'green':
            self.__color = 'yellow'
            sleep(5)
            if self.__flag_prev_color_green:
                print('Нельзя так переключать')
                exit(1)
            self.__flag_prev_color_green = True
        return self.__color

tl = TraficLight()
print(tl.running())
print(tl.running())
print(tl.running())
print(tl.running())
tl._TraficLight__color = 'red'
print(tl.running())
tl._TraficLight__color = 'red'
print(tl.running())
print(tl.running())

