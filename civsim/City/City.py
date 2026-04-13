from typing import TYPE_CHECKING

from civsim.City.House import House
from civsim.City.Systems.BuildSystem import BuildSystem
from civsim.City.Systems.HousingSystem import HousingSystem
from civsim.City.Systems.PopulationSystem import PopulationSystem
from civsim.City.Systems.WorkSystem import WorkSystem
from civsim.City.Workplace.EResources import EResources
from civsim.City.Workplace.Workplace import Workplace
from civsim.Human.Human import Human
from civsim.Mayor.Mayor import Mayor

if TYPE_CHECKING:
    from civsim.GameMaster import GameMaster

class City:
    def __init__(self, numOfCity: int, startPopulation: int, gm: GameMaster, mayor: Mayor = None):
        self.name = f"District {numOfCity}"
        self.houses = []
        self.population = []
        self.workplaces = []
        self.storage = {EResources.FOOD: 0, EResources.BRICKS: 0}
        self.year = gm.year
        self.peopleToKill = []
        self.populationSystem = PopulationSystem(self)
        self.housingSystem = HousingSystem(self)
        self.workplaceSystem = WorkSystem(self)
        self.buildSystem = BuildSystem(self)
        self.mayor = mayor
        self.spawnCity(startPopulation)

    def spawnCity(self, startPopulation: int):
        for i in range(startPopulation // 2):
            house = House()
            self.houses.append(house)

        for i in range(startPopulation):
            human = Human(15, city = self, birthYear = self.year)
            human.isAdult = True
            self.population.append(human)

        self.workplaces.append(Workplace(EResources.FOOD, self))
        self.workplaces.append(Workplace(EResources.BRICKS, self))

        self.populationSystem.updatePopulation()
        self.workplaceSystem.assignWorkplace()

    def updateCity(self):
        self.year += 1
        self.populationSystem.updatePopulation()
        self.housingSystem.accommodatePeople()
        self.workplaceSystem.updateWork()

