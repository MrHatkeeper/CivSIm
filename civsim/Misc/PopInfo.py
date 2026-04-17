from typing import TYPE_CHECKING

from civsim.Misc import EconInfo

if TYPE_CHECKING:
    from civsim.City.City import City

def getAdults(city: City):
    """
    Metoda vrátí všecnhy dospělé lidi ve městě.
    :param city: město, ve kterém metoda hledá.
    :return: pole dospělých lidí
    """
    return [human for human in city.population if human.isAdult]

def getUnemployed(city: City):
    """
    Metoda vrátí všechny nezaměstnané lidi ve městě.
    :param city: město, ve kterém metoda hledá.
    :return: pole nezaměstnaných
    """
    return [human for human in city.population if human.workplace is None and human.isAdult]

def getChildren(city: City):
    """
    Metoda vrátí všechny děti ve městě
    :param city: město, ve kterém metoda hledá.
    :return: pole dětí
    """
    return [human for human in city.population if not human.isAdult]

def numOfHomeless(city: City):
    """
    Metoda vratí počet bezdomovců ve městě
    :param city: město, ve kterém metoda hledá.
    :return: počet bezdomovců
    """
    return len(city.population) - EconInfo.numOfOccupiedLivingSpaces(city)