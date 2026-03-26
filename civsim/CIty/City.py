from civsim.CIty.House import House
from civsim.Human.Human import Human


class City:
    def __init__(self, numOfCity: int, startPopulation: int):
        self.name = f"District {numOfCity}"
        self.houses = []
        self.population = []
        self.spawnCity(startPopulation)

    def updateCity(self):
        self.giveHousesToPeople()

    def spawnCity(self, startPopulation: int):
        for i in range(startPopulation // 2):
            house = House(4)
            self.houses.append(house)

        for i in range(startPopulation):
            human = Human(15)

    def giveHousesToPeople(self):
        emptyHouses = self.getEmptyHouses()
        for human in self.population:
            if human.house is None:
                human.house = emptyHouses[-1]
                if emptyHouses[-1].resident.count == emptyHouses[-1].capacity:
                    emptyHouses.pop(-1)

    def getEmptyHouses(self):
        output = []
        for house in self.houses:
            if house.residents.count < house.capacity:
                output.append(house)
        return output