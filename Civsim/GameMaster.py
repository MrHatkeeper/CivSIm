from Civsim.City.City import City
from Civsim.Mayor.Mayor import Mayor
from Civsim.SaveManager.Loader import Loader
from Civsim.SaveManager.Saver import Saver


class GameMaster:
    def __init__(self):
        self.cities = []
        self.year = 0
        self.isRunning = False
        self.mayors = []
        self.speed = 1
        self.speedMultiplier = 1
        self.saver = Saver()
        self.loader = Loader(self)
        self.historyData = {}

    def crateSimulation(self, numOfStartingCities):
        """
        Funkce nastaví základní stav simulace.
        :param numOfStartingCities: počet měst na začátku.
        """
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
        """
        Funkce posune simulaci o rok dopředu.
        :return:
        """
        self.year += 1
        for mayor in self.mayors:
            if len(mayor.city.population) != 0:
                mayor.decision()


    def getSpeed(self):
        """
        Funkce vypočítá rychlost běhu simulace
        :return: rychlost běhu
        """
        return 1/self.speedMultiplier**2 * self.speed