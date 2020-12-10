class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} едет'.format(self.name))

    def stop(self):
        print('{} останавливается'.format(self.name))

    def turn(self, direction):
        print('{} поварачивает {}!'.format(self.name, direction))

    def show_speed(self):
        print('Текущая скорость:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Текущая скорость больше максимальной!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 40:
            print('Текущая скорость больше максимальной!')


class PoliceCar(Car):
    pass


sport_car = SportCar(250, 'Желтая', 'Спортивная машина', False)
town_car = TownCar(130, 'Белая', 'Городская машина', False)
work_car = WorkCar(100, 'Синяя', 'Рабочая машина', False)
police_car = PoliceCar(200, 'Синяя', 'Полицейская машина', True)

sport_car.show_speed()
work_car.show_speed()
town_car.turn('направо')
police_car.show_speed()
