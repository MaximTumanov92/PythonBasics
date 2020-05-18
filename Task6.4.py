from time import sleep


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def start(self):
        return f"{self.name} has started"

    def stop(self):
        return f"{self.name} has stopped"

    def turn(self):
        return f"{self.name} has turned"

    def speed(self):
        return f"{self.name} speed is {self.speed:.2f} km/h"

    def speed_rate(self):
        return f"{self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Speed of a Town car {self.name} is {self.speed:.2f} km/h")

        if self.speed > 60:
            return f"{self.name} is breaking the speed limit by {self.speed - 60:.2f} km/h"
        else:
            return f"Speed of {self.name} is in limit. Keep going that way"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Speed of a Work car {self.name} is {self.speed:.2f} km/h")

        if self.speed > 40:
            return f"{self.name} is breaking the speed limit by {self.speed - 40:.2f} km/h"
        else:
            return f"Speed of {self.name} is in limit. Keep going that way"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} is a police car. Watch out!"
        else:
            return f"{self.name} is not a police car"


Mercedes = TownCar(int(input("Input TownCar speed: ")), "Black", "Mercedes", False)
Ferrari = SportCar(200, "Red", "Ferrari", False)
Gazel = WorkCar(40, "Grey", "Gazel", False)
Priora = PoliceCar(50, "Grey", "Priora", True)

print(Mercedes.start())
print(Mercedes.turn())
print(Mercedes.show_speed())
if int(Car.speed_rate(Mercedes)) > 60:
    print(Priora.start())
    print(Priora.police())
    print(f"{Mercedes.color} {Mercedes.name} pull over!")
