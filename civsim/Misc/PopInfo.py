from typing import TYPE_CHECKING

from civsim.Misc import EconInfo

if TYPE_CHECKING:
    from civsim.City.City import City

def getAdults(city: City):
    return [human for human in city.population if human.isAdult]

def getUnemployed(city: City):
    return [human for human in city.population if human.workplace is None and human.isAdult]

def getChildren(city: City):
    return [human for human in city.population if not human.isAdult]

def numOfHomeless(city: City):
    return len(city.population) - EconInfo.numOfOccupiedLivingSpaces(city)