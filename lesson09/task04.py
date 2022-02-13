# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    __speed = 0
    __color = ''
    __name = ''
    __is_police = False

    def get_speed(self):
        return self.__speed

    def get_color(self):
        return self.__color

    def get_name(self):
        return self.__name

    def __init__(self, color, name):
        self.__color = color
        self.__name = name

    def go(self, speed):
        self.__speed = speed
        print(f'{self.__color} {self.__name} is moving at a speed of {self.__speed} km/h')

    def stop(self):
        self.__speed = 0
        print(f'{self.__color} {self.__name} stopped')

    def turn(self, direction):
        if direction.lower() in ('left', 'right'):
            print(f'{self.__color} {self.__name} turned to {direction}')

    def show_speed(self):
        print(f'current speed  {self.get_color()} {self.get_name()}  = {self.get_speed()} km/h')


class TownCar(Car):
    __max_allowed_speed = 60

    def show_speed(self):
        Car.show_speed(self)
        if self.get_speed() > self.__max_allowed_speed:
            print(f'alarm speed {super().get_speed()} to high for town car')


class WorkCar(Car):
    __max_allowed_speed = 40

    def show_speed(self):
        Car.show_speed(self)
        if self.get_speed() > self.__max_allowed_speed:
            print(f'alarm! speed {self.get_speed()} to high for work car')


class PoliceCar(Car):
    __is_police = True

    def __init__(self, name):
        super().__init__('White', name)

print('WorkCar:')
workcar = WorkCar('Green', 'Man')
workcar.go(50)
workcar.show_speed()
workcar.turn('left')
workcar.stop()
workcar.show_speed()

print('\nPoliceCar:')
policecar = PoliceCar('Renault')
policecar.go(120)
policecar.show_speed()

print('\nTownCar:')
towncar = TownCar('Red', 'Mersedes')
towncar.go(50)
towncar.show_speed()
towncar.go(90)
towncar.turn('right')
towncar.show_speed()
towncar.stop()
towncar.show_speed()
