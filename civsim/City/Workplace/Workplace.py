from typing import TYPE_CHECKING
from civsim.City.Workplace.EResources import EResources
from civsim.EConfig import EConfig

if TYPE_CHECKING:
    from civsim.City.City import City

class Workplace:
    def __init__(self, capacity: int, resource: EResources, city: City):
        self.ratio = EConfig.PRODURATIO.value
        self.capacity = capacity
        self.workforce = []
        self.resource = resource
        self.city = city

    def produceResource(self):
        if self.resource == EResources.FOOD:
            self.city.storage["Food"] += len(self.workforce) * self.ratio
        if self.resource == EResources.BRESOURCES:
            self.city.storage["BResources"] += len(self.workforce) * self.ratio