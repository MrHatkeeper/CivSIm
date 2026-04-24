from typing import TYPE_CHECKING

from streamlit import exception

from civsim.City.House import House
from civsim.City.Workplace.EResources import EResources
from civsim.City.Workplace.Workplace import Workplace
from civsim.Config import Config
from civsim.Misc import EconInfo

if TYPE_CHECKING:
    from civsim.City.City import City


class BuildSystem:
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
