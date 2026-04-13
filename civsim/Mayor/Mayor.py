from copy import deepcopy

from civsim.City.Workplace.EResources import EResources
from civsim.Config import Config
from civsim.Misc import CityInfo

def evalScore(cityState):
    population = len(cityState.population)

    if population == 0:
        return 0
    avg_hunger = CityInfo.getAverage("hunger", cityState)
    avg_happiness = CityInfo.getAverage("happiness", cityState)

    homeless_ratio = CityInfo.numOfHomeless(cityState) / population
    free_housing_ratio = CityInfo.numOfFreeLivingSpaces(cityState) / population

    hungerScore = -avg_hunger * Config.AVG_HUNGER_MULT.value
    happinessScore = avg_happiness * Config.AVG_HAPPINESS_MULT.value
    homelessScore = -homeless_ratio * Config.HOMELESS_MULT.value
    housingScore = free_housing_ratio * Config.FREE_HOUSING_SPACE_MULT.value

    return hungerScore + happinessScore + homelessScore + housingScore


def makeAction(action, cityState):
    if action == "buildHouse":
        if cityState.buildSystem.canBuild("house"):
            cityState.buildSystem.buildHouse()
    elif action == "buildFarm":
        if cityState.buildSystem.canBuild("farmHouse"):
            cityState.buildSystem.buildWorkplace(EResources.FOOD)
    elif action == "buildBrickHouse":
        if cityState.buildSystem.canBuild("brickHouse"):
            cityState.buildSystem.buildWorkplace(EResources.BRICKS)


class Mayor:
    def __init__(self, city):
        self.city = city
        self.lastAction = "nothing"

    def decision(self):
        actions = ["nothing", "buildHouse", "buildFarm", "buildBrickHouse"]
        startState = deepcopy(self.city)

        bestAction = actions[0]
        bestValue = evalScore(startState)
        for action in actions:
            simulatedCity = deepcopy(self.city)
            makeAction(action, simulatedCity)

            for lookAhead in range(Config.MAYOR_LOOK_AHEAD.value):
                simulatedCity.updateCity()

            evalValue = evalScore(simulatedCity)
            if evalValue > bestValue:
                bestAction = action
                bestValue = evalValue

        makeAction(bestAction, startState)
        self.city.updateCity()
        self.lastAction = bestAction

