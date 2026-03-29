from civsim.City.City import City


class GameMaster:
    def __init__(self):
        self.cities = []
        self.year = 0

    def startSimulation(self, numOfStartingCities):
        del self.cities[:]
        self.cities = []
        for i in range(numOfStartingCities):
            city = City(i, 4, self.year)
            self.cities.append(city)
