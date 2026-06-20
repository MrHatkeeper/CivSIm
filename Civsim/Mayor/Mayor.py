from copy import deepcopy
from math import inf

from Civsim.City.MockCity import MockCity
from Civsim.City.Workplace.EResources import EResources
from Civsim.Config import Config


def evalScore(cityState: MockCity):
    population = cityState.population
    happinessScore = cityState.avgHappiness * Config.AVG_HAPPINESS_MULT.value

    portion = cityState.getPortion()

    if portion >= 1:
        foodScore = (portion - 1) * Config.AVG_HUNGER_MULT.value
    else:
        foodScore = -(1 - portion) * Config.AVG_HUNGER_MULT.value

    homeless = max(cityState.population - cityState.occupiedHousing, 0)
    homelessRatio = homeless / population

    freeHousing = max(cityState.occupiedHousing - cityState.population, 0)
    freeHousingRatio = freeHousing / population

    homelessScore = -homelessRatio * Config.HOMELESS_MULT.value
    housingScore = freeHousingRatio * Config.FREE_HOUSING_SPACE_MULT.value

    return happinessScore + foodScore + homelessScore + housingScore


def makeAction(action, cityState):
    """
    Metoda postaví budovu v cityState.
    :param action: str
    :param cityState: City()
    """
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
            "nothing": 0,
            "buildHouse": 0,
            "buildFarm": 0,
            "buildBrickHouse": 0,
        }

    def canBuild(self, action) -> bool:
        if action == "buildHouse":
            return self.city.buildSystem.canBuild("house")
        if action == "buildFarm":
            return self.city.buildSystem.canBuild("farmHouse")
        if action == "buildBrickHouse":
            return self.city.buildSystem.canBuild("brickHouse")
        return True

    def decision(self):
        """
        Funkce vyzkouší možné stavy, jak jaká akce ovlivní mésto. Následně vybere a udělá tu nejlepší.
        """
        bestValue = -inf
        bestAction = list(self.actionValues.keys())[0]
        for action in self.actionValues.keys():
            startState = MockCity(self.city)
            evalValue = -1
            if action != "nothing":
                if self.canBuild(action):
                    startState.mockAction(action)
                    for lookAhead in range(Config.MAYOR_LOOK_AHEAD.value):
                        startState.updateMockCity()

                    evalValue = evalScore(startState)
            else:
                for lookAhead in range(Config.MAYOR_LOOK_AHEAD.value):
                    startState.updateMockCity()
                evalValue = evalScore(startState)
            self.actionValues[action] = evalValue
            if evalValue > bestValue:
                bestAction = action
                bestValue = evalValue

        makeAction(bestAction, self.city)
        self.city.updateCity()
        self.lastAction = bestAction
