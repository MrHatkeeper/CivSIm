from civsim.City.Workplace.EResources import EResources
from civsim.Config import Config
from civsim.Misc import EconInfo, Metrics


class MockCity:
    def __init__(self, city):
        self.city = city
        self.production = EconInfo.getProduction(city)
        self.population = len(city.population)
        self.occupiedHousing = EconInfo.numOfOccupiedLivingSpaces(city)
        self.freeHousing = EconInfo.numOfFreeLivingSpaces(city)

        self.avgHunger = Metrics.getAverage("hunger", city)
        self.avgHappiness = Metrics.getAverage("happiness", city)

    def updateMockCity(self):
        self.updateMockPopulation()
        self.mockAvgHappiness()

    def updateMockPopulation(self):
        if self.freeHousing != 0:
            self.occupiedHousing += self.freeHousing
            self.freeHousing = 0
        #TODO

    def mockAvgHappiness(self):
        homelessRatio = Config.IS_HOUSED_INC.value * (self.population - self.occupiedHousing)
        portion = (self.production[EResources.FOOD] / self.population) / Config.HUNGER_RATE.value
        if portion < 1:
            portion = Config.HUNGRY_INC.value * portion * -1

        self.avgHappiness = self.avgHappiness + -1 * homelessRatio + portion

    def mockAction(self, action: str):
        if action == "buildHouse":
            self.freeHousing += Config.HOUSE_MAX_RESIDENTS.value
        elif action == "buildFarm":
            self.production[EResources.FOOD] += Config.WORKPLACE_MAX_RESIDENTS.value * Config.PROD_RATIO.value
        elif action == "buildBrickHouse":
            self.production[EResources.BRICKS] += Config.WORKPLACE_MAX_RESIDENTS.value * Config.PROD_RATIO.value
        self.updateMockCity()
