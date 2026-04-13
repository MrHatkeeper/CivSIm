from typing import TYPE_CHECKING


from civsim.City.Workplace.EResources import EResources
from civsim.Config import Config

if TYPE_CHECKING:
    from civsim.City.City import City


def numOfOccupiedWorkPlaces(city: City, prodType: EResources):
    out = 0
    for workplace in city.workplaces:
        if workplace.resource == prodType:
            out += len(workplace.workforce)
    return out

def numOfFreeWorkPlaces(city: City, prodType: EResources):
    out = 0
    for workplace in city.workplaces:
        if workplace.resource == prodType:
            out += Config.WORKPLACE_MAX_RESIDENTS.value - len(workplace.workforce)
    return out

def getProduction(city: City):
    out = {}
    for workplace in city.workplaces:
        if workplace.resource not in out:
            out[workplace.resource] = 0
        out[workplace.resource] += len(workplace.workforce) * workplace.ratio
    if len(out) == 0:
        raise Exception("No resources available")
    return out

def getConsumption(city: City):
    return Config.HUNGER_RATE.value * len(city.population)

def numOfFreeLivingSpaces(city: City):
    out = 0
    for house in city.houses:
        out += house.capacity - len(house.residents)
    return out

def numOfOccupiedLivingSpaces(city: City):
    out = 0
    for house in city.houses:
        out += len(house.residents)
    return out
