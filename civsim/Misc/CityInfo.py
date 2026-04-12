from numpy.f2py.auxfuncs import throw_error

from civsim.City.City import City
from civsim.EConfig import EConfig


def getAdults(city: City):
    return [human for human in city.population if human.isAdult]

def getUnemployed(city: City):
    return [human for human in city.population if human.workplace is None and human.isAdult]

def getChildren(city: City):
    return [human for human in city.population if not human.isAdult]

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

def numOfHomeless(city: City):
    return len(city.population) - numOfOccupiedLivingSpaces(city)

def getAverage(value: str, city: City):
    out = 0
    if value == 'happiness':
        for human in city.population:
            out += human.happiness
    if value == 'hunger':
        for human in city.population:
            out += human.hunger
    else:
        throw_error("Nonexistent value")
    return round(out / len(city.population),2)

def getHighest(value: str, city: City):
    out = 0
    if value == 'happiness':
        for human in city.population:
            if human.happiness > out:
                out = human.happiness
    if value == 'hunger':
        for human in city.population:
            if human.hunger > out:
                out = human.hunger
    else:
        throw_error("Nonexistent value")
    return out

def getLowest(value: str, city: City):
    out = 0
    if value == 'happiness':
        out = city.population[0].happiness
        for human in city.population:
            if human.happiness < out:
                out = human.happiness
    if value == 'hunger':
        out = city.population[0].hunger
        for human in city.population:
            if human.hunger < out:
                out = human.hunger
    else:
        throw_error("Nonexistent value")
    return out

def getProduction(city: City):
    out = {}
    for workplace in city.workplaces:
        if workplace.resource not in out:
            out[workplace.resource] = 0
        out[workplace.resource] += len(workplace.workforce) * workplace.ratio
    return out

def getConsumption(city: City):
    return EConfig.HUNGERRATE.value * len(city.population)

