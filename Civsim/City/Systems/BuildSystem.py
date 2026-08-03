from typing import TYPE_CHECKING

from Civsim.City.House import House
from Civsim.City.Workplace.EResources import EResources
from Civsim.City.Workplace.Workplace import Workplace
from Civsim.Config import Config
from Civsim.Misc import EconInfo

if TYPE_CHECKING:
    from Civsim.City.City import City


class BuildSystem:
    """
    Reprezentace systému pro stavbu budov
    :param city: město, kterému patří
    """

    def __init__(self, city: City):
        self.city = city

    def canBuild(self, buildingType: str) -> bool:
        """
        Funkce vyhodnotí, zda budova, kterou chce Mayor() postavit, může být postavena.
        :param buildingType:
        :return bool
        """
        if buildingType == "brickHouse" or buildingType == "farmHouse":
            return self.city.storage[
                EResources.BRICKS] >= EconInfo.costToBuild(self.city, buildingType)
        if buildingType == "house":
            return self.city.storage[EResources.BRICKS] >= EconInfo.costToBuild(self.city, buildingType)
        raise TypeError("Invalid Build Type")

    def buildHouse(self):
        """
        V City(), kde je BuildSystem deklarován, přidá House().
        """
        self.city.storage[EResources.BRICKS] -= EconInfo.costToBuild(self.city, "house")
        self.city.houses.append(House())

    def buildWorkplace(self, resource: EResources):
        """
        V City(), kde je BuildSystem deklarován, přidá Workplace() s produkcí typu resource.
        :param resource: Typ produkce
        """
        self.city.storage[
            EResources.BRICKS] -= Config.WORKPLACE_COST.value * Config.WORKPLACE_COST_INC.value * EconInfo.numOfWorkplaces(
            self.city, resource)
        self.city.workplaces.append(Workplace(resource, self.city))
