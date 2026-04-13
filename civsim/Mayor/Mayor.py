from copy import deepcopy

from civsim.City.Workplace.EResources import EResources
from civsim.Config import Config
from civsim.Misc import EconInfo, Metrics, PopInfo


def evalScore(cityState):
    population = len(cityState.population)

    if population == 0:
        return 0
    avg_hunger = Metrics.getAverage("hunger", cityState)
    avg_happiness = Metrics.getAverage("happiness", cityState)

    homeless_ratio = PopInfo.numOfHomeless(cityState) / population
    free_housing_ratio = EconInfo.numOfFreeLivingSpaces(cityState) / population

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
        self.actionValues = {
            "nothing" : 0,
            "buildHouse" : 0,
            "buildFarm" : 0,
            "buildBrickHouse" : 0,
        }

    def decision(self):
        startState = deepcopy(self.city)

        bestAction = list(self.actionValues.keys())[0]
        bestValue = evalScore(startState)

        for action in self.actionValues.keys():
            simulatedCity = deepcopy(self.city)
            makeAction(action, simulatedCity)

            for lookAhead in range(Config.MAYOR_LOOK_AHEAD.value):
                simulatedCity.updateCity()

            evalValue = evalScore(simulatedCity)
            self.actionValues[action] = evalValue
            if evalValue > bestValue:
                bestAction = action
                bestValue = evalValue

        makeAction(bestAction, startState)
        self.city.updateCity()
        self.lastAction = bestAction

