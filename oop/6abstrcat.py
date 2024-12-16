#absreact class=cannot directly instanced on it own 
#abc-abstrcat based classes
from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod#abstractmethods doesnot have any definiation only declaration
    def stop(self):
        pass
    @abstractmethod#when u apply abstract methods in ur class u must use it in other inheritance class also 
    def go(self):
        pass
class car(vehicle):
    def stop(self):
        print("u need to stop")
    def go(self):
        print("u can go")

vehicle1=car()
vehicle1.stop()
vehicle1.go()