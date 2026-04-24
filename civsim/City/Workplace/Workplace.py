from typing import TYPE_CHECKING
from civsim.City.Workplace.EResources import EResources
from civsim.Config import Config

if TYPE_CHECKING:
    from civsim.City.City import City


class Workplace:
    def __init__(self, resource: EResources, city: City):
        self.ratio = Config.PROD_RATIO.value
        self.capacity = Config.WORKPLACE_MAX_RESIDENTS.value
        self.workforce = []
        self.resource = resource
        self.city = city

    def produceResource(self):
        """
        Funkce vyprodukuje svojí surovinu a přidá ji do skladu
        """
        self.city.storage[self.resource] += len(self.workforce) * self.ratio
