from civsim.City.City import City
from civsim.City.Workplace.EResources import EResources


class Workplace:
    def __init__(self, capacity: int, resource: EResources, city: City):
        self.ratio = 10
        self.capacity = capacity
        self.workforce = []
        self.resource = resource
        self.city = city

    def produceResource(self):
        if self.resource == EResources.FOOD:
            self.city.storage["Food"] += self.workforce * self.ratio
        if self.resource == EResources.BRESOURCES:
            self.city.storage["BResources"] += self.workforce * self.ratio