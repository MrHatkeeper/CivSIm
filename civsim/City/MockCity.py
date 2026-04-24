from civsim.City.Workplace.EResources import EResources
from civsim.Config import Config
from civsim.Misc import EconInfo, Metrics


class MockCity:
    def __init__(self, city):
        self.production = EconInfo.getProduction(city)
        self.population = len(city.population)
        self.occupiedHousing = EconInfo.numOfOccupiedLivingSpaces(city)
        self.freeHousing = EconInfo.numOfFreeLivingSpaces(city)

        self.avgHappiness = Metrics.getAverage("happiness", city)

    def updateMockCity(self):
        self.updateMockPopulation()
        self.mockAvgHappiness()

    def updateMockPopulation(self):
        if self.population == 0:
            return

        homeless = max(self.population - self.occupiedHousing, 0)
        toMove = min(homeless, self.freeHousing)

        self.occupiedHousing += toMove
        self.freeHousing -= toMove

        portion = self.getPortion()

        if portion < 1:
            starvation = (1 - portion)
            deaths = int(self.population * starvation * Config.STARVATION_RATE.value)
            self.population -= deaths
            self.occupiedHousing = min(self.occupiedHousing, self.population)

        elif portion > 1:
            growth = int(self.population * (portion - 1) * Config.GROWTH_RATE.value)

            self.population += growth

    def mockAvgHappiness(self):
        homelessRatio = max(self.population - self.occupiedHousing, 0) / self.population
        housingImpact = -homelessRatio * Config.IS_HOUSED_INC.value

        portion = (self.production[EResources.FOOD] / self.population) / Config.HUNGER_RATE.value
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
        return (self.production[EResources.FOOD] / self.population) / Config.HUNGER_RATE.value
