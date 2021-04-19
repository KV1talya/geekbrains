class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def go(self):
        print(f"машина {self.name} {self.color} поехала")

    def stop(self):
        print(f"машина {self.name} {self.color} остановилась")

    def turn(self, direction):
        print(f"машина {self.name} {self.color} повернула на {direction}")

    def show_speed(self):
        print(f"Скорость {self.speed}")


class TownCar(Car):
    speed = 61
    color = 'red'
    name = 'Toyota'

    def show_speed(self):
        if self.speed > 60:
            print("превышении скорости")


class SportCar(Car):
    speed = 100
    color = 'Red'
    name = 'Bugatti'


class WorkCar(Car):
    speed = 45
    color = 'Мокрый асфальт'
    name = 'Ваз'

    def show_speed(self):
        if self.speed > 40:
            print("превышении скорости")


class PoliceCar(Car):
    speed = 100
    color = 'Red'
    name = 'Bugatti'
    is_police = True


town = TownCar()
town.go()
town.show_speed()
town.turn("лево")
town.stop()
print(town.is_police)

sport = SportCar()
sport.go()
sport.show_speed()
sport.turn("право")
sport.stop()

police = PoliceCar()
print(police.is_police)
