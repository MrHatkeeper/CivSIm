from typing import TYPE_CHECKING

from streamlit import exception

from civsim.City.House import House
from civsim.City.Workplace.EResources import EResources
from civsim.City.Workplace.Workplace import Workplace
from civsim.Config import Config

if TYPE_CHECKING:
    from civsim.City.City import City

class BuildSystem:
    def __init__(self, city: City):
        self.city = city

    def canBuild(self, buildingType: str) -> bool:
        if buildingType == "brickHouse" or buildingType == "farmHouse":
            return self.city.storage[EResources.BRICKS] >= Config.WORKPLACE_COST.value
        if buildingType == "house":
            return self.city.storage[EResources.BRICKS] >= Config.HOUSE_COST.value
        raise TypeError("Invalid Build Type")

    def buildHouse(self):
        self.city.houses.append(House())

    def buildWorkplace(self, resource: EResources):
        self.city.workplaces.append(Workplace(resource, self.city))