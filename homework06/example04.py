class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.current_speed = 0
        self.is_police = False

    def go(self):
        self.current_speed = self.speed
        print("Car is moving")

    def stop(self):
        self.current_speed = 0
        print("Car has stopped")

    def turn(self, direction):
        print("Car turned " + direction)

    def show_speed(self):
        print("The speed is " + str(self.current_speed))


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.current_speed > 60:
            print("Speed limit is violated")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.current_speed > 40:
            print("Speed limit is violated")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


my_town_car = TownCar(80, "green", "Kodiaq")
my_town_car.turn("right")
my_town_car.show_speed()
my_town_car.go()
my_town_car.show_speed()


my_work_car = WorkCar(35, "red", "A6 Avant")
my_work_car.turn("right")
my_work_car.go()
my_work_car.show_speed()


