import uuid
from typing import TYPE_CHECKING

from Civsim.City.Workplace.EResources import EResources
from Civsim.Config import Config

if TYPE_CHECKING:
    from Civsim.City.City import City


class Workplace:
    """
    Reprezentace jedné dílny
    :param:
    resource: typ suroviny
    city: město, kterému patří
    """

    def __init__(self, resource: EResources, city: City):
        self.id = uuid.uuid4()
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
