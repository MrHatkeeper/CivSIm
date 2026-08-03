from typing import TYPE_CHECKING

from Civsim.Misc import EconInfo

if TYPE_CHECKING:
    from Civsim.City.City import City


def getAdults(city: City):
    """
    Metoda vrátí všecnhy dospělé lidi ve městě.
    :param city: město, ve kterém metoda hledá.
    :return: pole dospělých lidí
    """
    return [human for human in city.population if human.adult]


def getUnemployed(city: City):
    """
    Metoda vrátí všechny nezaměstnané lidi ve městě.
    :param city: město, ve kterém metoda hledá.
    :return: pole nezaměstnaných
    """
    return [human for human in city.population if human.workplace is None and human.adult]


def getChildren(city: City):
    """
    Metoda vrátí všechny děti ve městě
    :param city: město, ve kterém metoda hledá.
    :return: pole dětí
    """
    return [human for human in city.population if not human.adult]


def numOfHomeless(city: City):
    """
    Metoda vratí počet bezdomovců ve městě
    :param city: město, ve kterém metoda hledá.
    :return: počet bezdomovců
    """
    return max(len(city.population) - EconInfo.numOfOccupiedLivingSpaces(city), 0)
