from typing import TYPE_CHECKING

from Civsim.City.Workplace.EResources import EResources
from Civsim.Config import Config
from Civsim.Misc import EconInfo, Metrics

if TYPE_CHECKING:
    from Civsim.City.City import City

class MockCity:
    def __init__(self, city: City):
        self.production = EconInfo.getProduction(city)
        self.population = len(city.population)
        self.occupiedHousing = EconInfo.numOfOccupiedLivingSpaces(city)
        self.freeHousing = EconInfo.numOfFreeLivingSpaces(city)
        self.storage = {EResources.FOOD: city.storage[EResources.FOOD], EResources: city.storage[EResources.BRICKS]}

        self.avgHappiness = Metrics.getAverage("happiness", city)

    def updateMockCity(self):
        self.accommodateMockPopulation()
        self.mockFeedPopulation()
        self.mockAvgHappiness()

    def mockFeedPopulation(self):
        portion = self.getPortion()

        if portion < 1:
            starvation = (1 - portion)
            deaths = int(self.population * starvation * Config.STARVATION_RATE.value)
            self.population -= deaths
            self.occupiedHousing = min(self.occupiedHousing, self.population)

        elif portion > 1:
            growth = int(self.population * (portion - 1) * Config.GROWTH_RATE.value)

            self.population += growth
        self.storage[EResources.FOOD] - portion * self.population

    def accommodateMockPopulation(self):
        if self.population == 0:
            return

        homeless = max(self.population - self.occupiedHousing, 0)
        toMove = min(homeless, self.freeHousing)

        self.occupiedHousing += toMove
        self.freeHousing -= toMove

    def mockAvgHappiness(self):
        homelessRatio = max(self.population - self.occupiedHousing, 0) / self.population
        housingImpact = -homelessRatio * Config.IS_HOUSED_INC.value

        portion = self.getPortion()
        hungerImpact = Config.HUNGRY_INC.value * (portion - 1)

        self.avgHappiness += housingImpact + portion * hungerImpact

    def mockAction(self, action: str):
        if action == "buildHouse":
            self.freeHousing += Config.HOUSE_MAX_RESIDENTS.value
        elif action == "buildFarm":
            self.production[EResources.FOOD] += Config.WORKPLACE_MAX_RESIDENTS.value * Config.PROD_RATIO.value
        elif action == "buildBrickHouse":
            self.production[EResources.BRICKS] += Config.WORKPLACE_MAX_RESIDENTS.value * Config.PROD_RATIO.value
        self.updateMockCity()

    def getPortion(self):
        return ((self.production[EResources.FOOD] + self.storage[
            EResources.FOOD]) / self.population) / Config.HUNGER_RATE.value
