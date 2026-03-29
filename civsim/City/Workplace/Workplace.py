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
        self.city.storage[self.resource] += len(self.workforce) * self.ratio