from civsim.City.City import City


class GameMaster:
    def __init__(self):
        self.cities = []
        self.year = 0
        self.isRunning = False

    def startSimulation(self, numOfStartingCities):
        del self.cities[:]
        self.cities = []
        self.isRunning = True
        self.year = 0
        for i in range(numOfStartingCities):
            city = City(i, 4, self.year)
            self.cities.append(city)

    def moveOneYear(self):
        self.year += 1
        for city in self.cities:
            city.updateCity()