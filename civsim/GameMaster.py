from civsim.City.City import City
from civsim.Mayor.Mayor import Mayor


class GameMaster:
    def __init__(self):
        self.cities = []
        self.year = 0
        self.isRunning = False
        self.mayors = []

    def startSimulation(self, numOfStartingCities):
        del self.cities[:]
        self.cities = []
        self.isRunning = True
        self.year = 0
        for i in range(numOfStartingCities):
            city = City(i, 4, self)
            mayor = Mayor(city)
            city.mayor = mayor
            self.mayors.append(mayor)
            self.cities.append(city)

    def moveOneYear(self):
        self.year += 1
        for mayor in self.mayors:
            mayor.decision()
