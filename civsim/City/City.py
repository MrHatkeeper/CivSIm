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
        self.storage = {EResources.FOOD: 0, EResources.BRESOURCES: 0}
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
        portion = self.storage[EResources.FOOD] / len(self.population)
        for human in self.population:
            human.updateHuman()
            if human.hunger < portion:
                newPortion = human.hunger
                human.hunger -= newPortion
                self.storage[EResources.FOOD] -= newPortion
            else:
                human.hunger -= portion
                self.storage[EResources.FOOD] -= portion

    def updateResources(self):
        for workplace in self.workplaces:
            workplace.produceResource()

    def spawnCity(self, startPopulation: int):
        for i in range(startPopulation // 2):
            house = House(4)
            self.houses.append(house)

        for i in range(startPopulation):
            human = Human(15, city = self)
            human.isAdult = True
            self.population.append(human)
        self.workplaces.append(Workplace(2, EResources.FOOD, self))
        self.workplaces.append(Workplace(2, EResources.BRESOURCES, self))
        self.giveHousesToPeople()
        self.assignWorkplace()

    def giveHousesToPeople(self):
        emptyHouses = self.getEmptyHouses()
        for human in self.population:
            if human.house is None:
                human.house = emptyHouses[0]
                emptyHouses[0].residents.append(human)
                if len(emptyHouses[0].residents) == emptyHouses[0].capacity:
                    emptyHouses.pop(0)

    def getEmptyHouses(self):
        output = []
        for house in self.houses:
            if len(house.residents) < house.capacity:
                output.append(house)
        return output

    def assignWorkplace(self):
        from civsim.Misc import CityInfo
        unemployed = CityInfo.getUnemployed(self)
        for workplace in self.workplaces:
            if len(unemployed) == 0:
                break
            freeSlots = workplace.capacity - len(workplace.workforce)
            if freeSlots > 0:
                toAssign = unemployed[:freeSlots]
                for human in toAssign:
                    human.workplace = workplace
                    workplace.workforce.append(human)
                unemployed = unemployed[freeSlots:]

