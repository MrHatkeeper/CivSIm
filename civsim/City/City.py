from typing import Tuple

from civsim.City.House import House
from civsim.City.Workplace.EResources import EResources
from civsim.City.Workplace.Workplace import Workplace
from civsim.Human.Human import Human


class City:
    def __init__(self, numOfCity: int, startPopulation: int, year: int):
        self.name = f"District {numOfCity}"
        self.houses = []
        self.population = []
        self.workplaces = []
        self.storage = {"Food": 0, "BResources": 0}
        self.spawnCity(startPopulation)
        self.year = year
        self.peopleToKill = []

    def updateCity(self):
        self.updateResources()
        self.updatePeople()
        self.assignWorkplace()

    def killPeople(self):
        for human in self.peopleToKill:
            human.house.residents.remove(human)
            human.workplace.workforce.remove(human)
            human.population.remove(human)
            del human

    def updatePeople(self):
        self.giveHousesToPeople()
        self.updatePopulation()
        self.killPeople()

    def updatePopulation(self):
        portion = self.storage["Food"] / len(self.population)
        for human in self.population:
            human.updateHuman()
            if human.hunger < portion:
                newPortion = human.hunger
                human.hunger -= newPortion
                self.storage["Food"] -= newPortion
            else:
                human.hunger -= portion
                self.storage["Food"] -= portion

    def updateResources(self):
        for workplace in self.workplaces:
            workplace.updateResources()

    def spawnCity(self, startPopulation: int):
        for i in range(startPopulation // 2):
            house = House(4)
            self.houses.append(house)

        for i in range(startPopulation):
            human = Human(15, city = self)
        self.workplaces.append(Workplace(2, EResources.FOOD, self))
        self.workplaces.append(Workplace(2, EResources.BRESOURCES, self))

    def giveHousesToPeople(self):
        emptyHouses = self.getEmptyHouses()
        for human in self.population:
            if human.house is None:
                human.house = emptyHouses[0]
                if emptyHouses[0].resident.count == emptyHouses[0].capacity:
                    emptyHouses.pop(0)

    def getEmptyHouses(self):
        output = []
        for house in self.houses:
            if house.residents.count < house.capacity:
                output.append(house)
        return output

    def assignWorkplace(self):
        for workplace in self.workplaces:
            if len(workplace.workforce) < workplace.capacity:
                toHire = workplace.capacity - len(workplace.workforce)
                for human in self.population:
                    if toHire == 0:
                        break
                    if human.workplace is None and human not in self.peopleToKill and human.isAdult:
                        human.workplace = workplace
                        toHire -= 1