import random
from prac_09.car import Car

class UnreliableCar(Car):
    """A car that may not always drive based on its reliability"""

    def __init__(self, name, fuel, reliability):
        """Initialize an unreliable car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Only drive the car if random number is less than reliability"""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
