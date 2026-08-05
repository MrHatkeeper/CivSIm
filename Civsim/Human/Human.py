import random
import uuid
from typing import TYPE_CHECKING

from Civsim.Config import Config

if TYPE_CHECKING:
    from Civsim.City.City import City


class Human:
    """
    Reprezentace jednoho člověka ve městě.

    :param startAge: v jakém věku se člověk má objevit
    :param city: ve kterém městě je
    :param birthYear: v jakém roce se člověk narodil
    """

    def __init__(self, startAge: int = 0, city: City = None, birthYear: int = None):
        self.id = uuid.uuid4()
        self.startAge = startAge
        self.age = startAge
        self.hungerRate = Config.HUNGER_RATE.value
        self.happiness = 100
        self.hunger = 0
        self.house = None
        self.adult = False
        self.city = city
        self.workplace = None
        self.birthDate = birthYear
        self.isAdult()

    def updateHuman(self):
        """
        Zestárne člověka, přidá mu hlad, zjistí, jak moc je šťastný a popřípadě ho přidá do seznamu lidí na zabití.
        """
        self.age = self.startAge + self.city.year - self.birthDate
        self.isAdult()
        self.hunger += self.hungerRate
        self.evalHappiness()
        self.killHuman()

    def isAdult(self):
        """
        Vyhodnocuje, zda je již člověk dospělý
        """
        self.adult = self.age >= Config.ADULT_AGE.value

    def killHuman(self):
        """
        Zjistí, zda člověk má umřít
        """
        if self.happiness < Config.DEATH_BORDER.value:
            rand = random.randrange(1, 100)
            if rand < 50 or self.happiness <= 0 or self.hunger >= 10:
                self.city.peopleToKill.append(self)

    def evalHappiness(self):
        """
        Aktualizuje happiness podle momentálního stavu člověka.
        """
        if self.house is None:
            self.happiness -= Config.IS_HOUSED_INC.value
        else:
            self.happiness += Config.IS_HOUSED_INC.value

        self.happiness += (
            self.hunger * -1
        ) * Config.HUNGRY_INC.value + Config.HUNGRY_INC.value
        self.happiness = max(0, min(self.happiness, 100))

    def reproduce(self):
        """
        Funkce vyhodnotí, zda se člověk má rozmnožit, popřípadě vytvoří dítě.
        """
        if not self.adult:
            return
        partner = None
        if self.house is not None:
            for resident in self.house.residents:
                if resident is not self and resident.adult:
                    partner = resident
                    break
        else:
            for human in self.city.population:
                if human is not self and human.adult and human.house is None:
                    partner = human
                    break
        if partner is None:
            return
        if id(self) > id(partner):
            return
        base_chance = Config.BIRTH_RATIO.value
        happiness_factor = (self.happiness + partner.happiness) / 2
        if self.house is not None:
            chance = base_chance * (happiness_factor / 100)
        else:
            chance = (
                base_chance
                * Config.HOMELESS_BIRTH_RATIO.value
                * (happiness_factor / 100)
            )
        if random.random() * 100 < chance:
            baby = Human(0, city=self.city, birthYear=self.city.year)

            baby.house = None
            baby.hunger = (self.hunger + partner.hunger) / 2
            if (
                self.house is not None
                and len(self.house.residents) < self.house.capacity
            ):
                baby.house = self.house
                self.house.residents.append(baby)
            self.city.population.append(baby)
