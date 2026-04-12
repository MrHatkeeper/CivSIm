import random

from civsim.City.House import House
from civsim.City.Systems.HousingSystem import HousingSystem
from civsim.City.Systems.PopulationSystem import PopulationSystem
from civsim.City.Systems.WorkSystem import WorkSystem
from civsim.City.Workplace.EResources import EResources
from civsim.City.Workplace.Workplace import Workplace
from civsim.Human.Human import Human


class City:
    def __init__(self, numOfCity: int, startPopulation: int, year: int):
        self.name = f"District {numOfCity}"
        self.houses = []
        self.population = []
        self.workplaces = []
        self.storage = {EResources.FOOD: 0, EResources.BRICKS: 0}
        self.year = year
        self.peopleToKill = []
        self.populationSystem = PopulationSystem(self)
        self.housingSystem = HousingSystem(self)
        self.workplaceSystem = WorkSystem(self)
        self.spawnCity(startPopulation)

    def spawnCity(self, startPopulation: int):
        for i in range(startPopulation // 2):
            house = House(4)
            self.houses.append(house)

        for i in range(startPopulation):
            human = Human(15, city = self, birthYear = self.year)
            human.isAdult = True
            self.population.append(human)
        self.workplaces.append(Workplace(2, EResources.FOOD, self))
        self.workplaces.append(Workplace(2, EResources.BRICKS, self))
        self.populationSystem.updatePopulation()
        self.workplaceSystem.assignWorkplace()

    def updateCity(self):
        self.year += 1
        self.populationSystem.updatePopulation()
        self.housingSystem.accommodatePeople()
        self.workplaceSystem.updateWork()

