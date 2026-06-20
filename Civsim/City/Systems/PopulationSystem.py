import random
from typing import TYPE_CHECKING

from Civsim.City.Workplace.EResources import EResources

if TYPE_CHECKING:
    from Civsim.City.City import City

class PopulationSystem:
    def __init__(self, city: City):
        self.city = city

    def updatePopulation(self):
        """
        Aktualizuje stav populace.
        """
        for human in self.city.population:
            human.updateHuman()

        self.killPeople()

        for human in self.city.population:
            human.reproduce()

        self.feedPopulation()

    def feedPopulation(self):
        """
        Rozdělí, kolik kdo z populace dostane najíst.
        """
        random.shuffle(self.city.population)
        for human in self.city.population:
            if self.city.storage[EResources.FOOD] <= 0:
                break
            needed = human.hunger
            given = min(needed, self.city.storage[EResources.FOOD])
            human.hunger -= given
            self.city.storage[EResources.FOOD] -= given

    def killPeople(self):
        """
        Smaže Human(). kteří splňují podmínky na umření.
        """
        for human in self.city.peopleToKill:
            if human.house is not None and human in human.house.residents:
                human.house.residents.remove(human)
            if human.workplace is not None and human in human.workplace.workforce:
                human.workplace.workforce.remove(human)
            if human in human.city.population:
                human.city.population.remove(human)
        self.city.peopleToKill.clear()