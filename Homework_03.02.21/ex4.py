class Car:
    def __init__(self, name, color, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'Тапку в пол, едем вперед! \n {self.name} срывается с места')

    def stop(self):
        print(f'Кондуктор, нажми на тормоза... \n {self.name} мягко притармаживает')

    def turn_right(self):
        print(f'Напрво поедешь...\n {self.name} поворачивает направо')

    def turn_left(self):
        print(f'Лево руля!\n {self.name} поворачивает влево ')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Вы близки к нарушению, сбавьте скоротсь')

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Вы близки к нарушению, сбавьте скоротсь')

class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True

    def sound_da_police(self):
        print('Woop-woop! Thats the sound of da police Woop-woop! Thats the sound of da beast')

auto1 = TownCar('Ford Focus', 'голубой', 61, False)
auto1.show_speed()

auto2 = WorkCar('ZIL', 'white', 39, False)
auto2.show_speed()

auto3 = SportCar('Ford Mustang', 'black', 74, False)
auto3.go()
auto3.turn_left()
auto3.stop()

auto4 = PoliceCar('Toyota Corolla', 'blue&white', 50, True)
auto4.sound_da_police()


