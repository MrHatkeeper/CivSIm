from typing import TYPE_CHECKING

from Civsim.City.Workplace.EResources import EResources
from Civsim.Config import Config

if TYPE_CHECKING:
    from Civsim.City.City import City


def numOfWorkplaces(city: City, prodType: EResources):
    """
    Pomocná metoda pro získání počtu továren, co produkují jednu surovinu.
    :param city: město, ve kterém metoda hledá
    :param prodType: surovina, kterou metoda hledá
    :return: počet továren
    """
    out = 0
    for workplace in city.workplaces:
        if workplace.resource == prodType:
            out += 1
    return out


def numOfOccupiedWorkPlaces(city: City, prodType: EResources):
    """
    Pomocná metoda pro získání obsazených pracovních míst jedné suroviny.
    :param city: město, ve kterém metoda hledá
    :param prodType: surovina, kterou metoda hledá
    :return: počet obsazených pracovních míst jedné suroviny.
    """
    out = 0
    for workplace in city.workplaces:
        if workplace.resource == prodType:
            out += len(workplace.workforce)
    return out


def numOfFreeWorkPlaces(city: City, prodType: EResources):
    """
    Pomocná metoda pro získání volných pracovních míst jedné suroviny.
    :param city: město, ve kterém metoda hledá
    :param prodType: surovina, kterou metoda hledá
    :return: počet volných pracovních míst jedné suroviny.
    """
    out = 0
    for workplace in city.workplaces:
        if workplace.resource == prodType:
            out += Config.WORKPLACE_MAX_RESIDENTS.value - len(workplace.workforce)
    return out


def getProduction(city: City):
    """
    Pomocná funkce pro spočítání celkové produkce jednoho města všech surovin.
    :param city: město, ve kterém metoda hledá.
    :return: celková produkce
    """
    out = {}
    for resource in city.storage.keys():
        out[resource] = 0
    for workplace in city.workplaces:
        out[workplace.resource] += len(workplace.workforce) * workplace.ratio
    return out


def getConsumption(city: City):
    """
    Pomocná metoda pro spočítání celkové konsumpce jídla za rok.
    :param city: město, ve kterém metoda hledá.
    :return: počet jídla snězeného za rok,
    """
    return Config.HUNGER_RATE.value * len(city.population)


def numOfHouses(city: City):
    """
    Pomocná metoda vracející počet domů ve městě.
    :param city: město, ve kterém metoda hledá.
    :return: počet domů v jendom městě
    """
    return len(city.houses)


def numOfFreeLivingSpaces(city: City):
    """
    Pomocná metoda vracející počet volných míst k bydlení v jednom městě.
    :param city: město, ve kterém metoda hledá.
    :return: počet volných míst k bydlení
    """
    out = 0
    for house in city.houses:
        out += house.capacity - len(house.residents)
    return out


def numOfOccupiedLivingSpaces(city: City):
    """
    Pomocná funkce vracející počet obsazených míst k bydlení v jednom městě.
    :param city: město, ve kterém metoda hledá.
    :return: počet obsazených míst k bydlení v jednom městě.
    """
    out = 0
    for house in city.houses:
        out += len(house.residents)
    return out


def costToBuild(city: City, buildingType: str):
    """
    Funkce pro výpočet, kolik bude stát postavit danou budovu.
    :param city: ve kterém městě se má budova postavit
    :param buildingType: typ budovy
    :return: cena budovy
    """
    if buildingType == "brickHouse":
        return Config.WORKPLACE_COST.value * Config.WORKPLACE_COST_INC.value * numOfWorkplaces(city, EResources.BRICKS)
    if buildingType == "farmHouse":
        return Config.WORKPLACE_COST.value * Config.WORKPLACE_COST_INC.value * numOfWorkplaces(city, EResources.FOOD)
    if buildingType == "house":
        return Config.HOUSE_COST.value * Config.HOUSE_COST_INC.value * numOfHouses(city)
    raise TypeError("Invalid Build Type")
