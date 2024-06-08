from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.current_speed = 0

    def start_engine(self):
        return "car started"

    def stop_engine(self):
        return "car stopped"

class SportCar(Car):
    
    def start_engine(self):
        parent_message = super().start_engine()
        print("sport",parent_message)
        print(f"Sportcar max speed is {self.max_speed} km/h")
    
    def stop_engine(self):
        parent_message = super().stop_engine()
        print("sport",parent_message)
        self.current_speed = 0

my_car = Car(max_speed=200)
print(my_car.start_engine())  
print(my_car.stop_engine())  

my_sport_car = SportCar(max_speed=300)
my_sport_car.start_engine()  
my_sport_car.stop_engine()   