from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from civsim.City.City import City

def getAverage(value: str, city: City):
    """
    Pomocná metoda vrátí průměrnou hodnotu z města.
    :param value: hledaná hodnota
    :param city: město, ve kterém metoda hledá.
    :return: průměr hodnotu
    """
    out = 0
    if value == 'happiness':
        for human in city.population:
            out += human.happiness
    elif value == 'hunger':
        for human in city.population:
            out += human.hunger
    else:
        raise ValueError("Nonexistent value")
    return round(out / len(city.population),2)

def getHighest(value: str, city: City):
    """
    Pomocná metoda vrátí nejvyšší hodnotu z města.
    :param value: hledaná hodnota
    :param city: město, ve kterém metoda hledá.
    :return: nejvyšší hodnotu
    """
    out = 0
    if value == 'happiness':
        for human in city.population:
            if human.happiness > out:
                out = human.happiness
    elif value == 'hunger':
        for human in city.population:
            if human.hunger > out:
                out = human.hunger
    else:
        raise ValueError("Nonexistent value")
    return out

def getLowest(value: str, city: City):
    """
    Pomocná metoda vrátí nejnižší hodnotu z města.
    :param value: hledaná hodnota
    :param city: město, ve kterém metoda hledá.
    :return: nejnižší hodnotu
    """
    out = 0
    if value == 'happiness':
        out = city.population[0].happiness
        for human in city.population:
            if human.happiness < out:
                out = human.happiness
    elif value == 'hunger':
        out = city.population[0].hunger
        for human in city.population:
            if human.hunger < out:
                out = human.hunger
    else:
        raise ValueError("Nonexistent value")
    return out