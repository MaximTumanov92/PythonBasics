from time import sleep
from termcolor import colored


class TrafficLight:
    __color = ["Red", "Yellow", "Green", "Yellow"]
    __sleep = [7, 2, 10, 2]
    __paint = ["red", "yellow", "green", "yellow"]

    def running(self):
        i = 0
        while i <= 3:
            print(colored(f"{TrafficLight.__color[i]}", TrafficLight.__paint[i]))
            sleep(self.__sleep[i])
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
