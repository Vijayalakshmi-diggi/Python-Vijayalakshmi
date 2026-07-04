from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def sound(self):
        pass
class car(vehicle):
    def sound(self):
        print("smooth")
    def price(self):
        print("depent on brand")
class bike(vehicle):
    def sound(self):
        print("loud sound")
v1=car()
v1.sound()
v1.price()
v2=bike()
v2.sound()