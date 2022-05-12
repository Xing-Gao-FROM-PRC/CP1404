import random
from car import Car

class UnreliableCar(Car):
    
    def __init__(self, name, fuel, reliability):
        super().__init__(name,fuel)
        self.reliability = reliability
    
    def drive(self,distance):
        random_num = random.randint(1,100) 
        if random_num >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven