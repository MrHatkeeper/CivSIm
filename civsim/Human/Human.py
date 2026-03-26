from typing import Tuple
from civsim.City.City import City


class Human:
    def __init__(self, startAge: int = 0, hungerRate: float = 1, city: City = None, birthDate: int = None):
        self.name = self.generateName()
        self.age = startAge
        self.hungerRate = hungerRate
        self.happiness = 100
        self.hunger = 0
        self.house = None
        self.isAdult = False
        self.city = city
        self.workplace = None
        self.birthDate = birthDate

    def updateHuman(self):
        self.age = self.city.year - self.birthDate
        self.hunger += self.hungerRate
        self.happiness = self.evalHappiness()

    def evalHappiness(self):
        ...

    def giveBirth(self):
        ...

    def die(self):
        self.city.peopleToKill.append(self)

    #TODO:
    def generateName(self) -> str:
        return "A"