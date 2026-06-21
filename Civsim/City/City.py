from typing import TYPE_CHECKING


from Civsim.City.House import House
from Civsim.City.Systems.BuildSystem import BuildSystem
from Civsim.City.Systems.HousingSystem import HousingSystem
from Civsim.City.Systems.PopulationSystem import PopulationSystem
from Civsim.City.Systems.WorkSystem import WorkSystem
from Civsim.City.Workplace.EResources import EResources
from Civsim.City.Workplace.Workplace import Workplace
from Civsim.Human.Human import Human
from Civsim.Mayor.Mayor import Mayor

if TYPE_CHECKING:
    from Civsim.GameMaster import GameMaster


class City:
    def __init__(self, numOfCity: int, startPopulation: int, gm: GameMaster, mayor: Mayor = None):
        self.name = f"City {numOfCity}"
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
        """
        Nastaví městu výchozí stav.
        :param startPopulation: počet počátečních lidí
        """
        for i in range(startPopulation // 2):
            house = House()
            self.houses.append(house)

        for i in range(startPopulation):
            human = Human(15, city=self, birthYear=self.year)
            human.adult = True
            self.population.append(human)

        self.workplaces.append(Workplace(EResources.FOOD, self))
        self.workplaces.append(Workplace(EResources.BRICKS, self))

        self.populationSystem.updatePopulation()
        self.workplaceSystem.assignWorkplace()

    def updateCity(self):
        """
        Funkce zavolá všechny pomocné systémy na aktualizaci města.
        """
        self.year += 1
        self.populationSystem.updatePopulation()
        self.housingSystem.accommodatePeople()
        self.workplaceSystem.updateWork()

