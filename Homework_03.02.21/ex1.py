import time
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = (('RED', 7), ('YELLOW', 2), ('GREEN', 6))

    def running(self):
        for color, sec in cycle(self.__color):
            for i in range(sec):
                print(f'{color} for {sec}')
                sec -= 1
                time.sleep(1)


traffic_light = TrafficLight()
traffic_light.running()

# немного доработал условие задачи, теперь результат похож на светофор
