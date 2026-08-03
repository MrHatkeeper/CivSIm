from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Civsim.City.City import City


def accommodateHuman(human, house):
    """
    Pomoconá funkce pro přiřazení domu člověku.
    :param human: Human()
    :param house: House()
    """
    human.house = house
    house.residents.append(human)


class HousingSystem:
    """
    Reprezentace systému pro ubytovávání lidí
    :param city: město, kterému patří
    """

    def __init__(self, city: City):
        self.city = city

    def accommodatePeople(self):
        """
        Funkce přiřadí všem bezdomovcům dům, pokud jsou nějaké volné pokoje.
        """
        emptyHouses = [h for h in self.city.houses if len(h.residents) < h.capacity]
        houseIndex = 0
        for human in self.city.population:
            if human.house is not None:
                continue
            if houseIndex >= len(emptyHouses):
                break
            house = emptyHouses[houseIndex]
            accommodateHuman(human, house)
            if len(house.residents) >= house.capacity:
                houseIndex += 1
