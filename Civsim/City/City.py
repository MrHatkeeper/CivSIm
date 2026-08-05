from typing import TYPE_CHECKING

from Civsim.City.House import House
from Civsim.City.Systems.BuildSystem import BuildSystem
from Civsim.City.Systems.HistorySystem import HistorySystem
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
    """
    Reprezentace jednoho města
    :param
    numOfCities: kolikáté je to město
    startPopulation: s kolika obyvateli má město začínat
    gm: Správce světa
    mayor: který model se o město stará
    """

    def __init__(self, numOfCity: int, startPopulation: int, startYear: int, mayor: Mayor = None):
        self.name = f"City {numOfCity}"
        self.houses = []
        self.population = []
        self.workplaces = []
        self.storage = {EResources.FOOD: 0, EResources.BRICKS: 0}
        self.year = startYear
        self.peopleToKill = []
        self.populationSystem = PopulationSystem(self)
        self.housingSystem = HousingSystem(self)
        self.workplaceSystem = WorkSystem(self)
        self.buildSystem = BuildSystem(self)
        self.historySystem = HistorySystem(self)
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

        self.workplaceSystem.assignWorkplace()

    def updateCity(self):
        """
        Funkce zavolá všechny pomocné systémy na aktualizaci města.
        """
        self.year += 1
        self.workplaceSystem.updateWork()
        self.populationSystem.updatePopulation()
        self.housingSystem.accommodatePeople()
        self.historySystem.saveData()
