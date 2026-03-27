from civsim.City.City import City


class GameMaster:
    def __init__(self):
        self.cities = []
        self.cityNumber = 0
        self.year = 0

    def startSimulation(self, numOfStartingCities):
        del self.cities[:]
        self.cities = []
        for i in range(numOfStartingCities):
            self.addCity(i)

    def addCity(self, num):
        city = City(num,4, self.year)
        self.cities.append(city)
        self.cityNumber += 1