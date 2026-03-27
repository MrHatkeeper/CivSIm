import random
import math
from typing import TYPE_CHECKING

from civsim.EConfig import EConfig

if TYPE_CHECKING:
    from civsim.City.City import City

class Human:
    def __init__(self, startAge: int = 0, city: City = None, birthYear: int = None):
        self.name = self.generateName()
        self.age = startAge
        self.hungerRate = EConfig.HUNGERRATE.value
        self.happiness = 100
        self.hunger = 0
        self.house = None
        self.isAdult = False
        self.city = city
        self.workplace = None
        self.birthDate = birthYear

    def updateHuman(self):
        self.age = self.city.year - self.birthDate
        if self.age >= EConfig.ADULTAGE.value:
            self.isAdult = True
        self.hunger += self.hungerRate
        self.evalHappiness()

    def evalHappiness(self):
        if self.house is None:
            self.happiness -= EConfig.ISHOUSEDINC.value
        else:
            self.happiness += EConfig.ISHOUSEDINC.value

        self.happiness = self.happiness + (self.hunger * -1) * EConfig.HUNGRYINC.value + EConfig.HUNGRYINC.value
        if self.happiness > 100:
            self.happiness = 100

    def giveBirth(self):
        if len(self.house.residents) > 2:
            rand = random.randrange(1,100)
            if EConfig.BIRTHRATIO.value * math.log(len(self.house.residents)) <= rand:
                #Maybe a bit of fucky wacky, pokud se passuje reference a nevytváří nová proměnná
                human = Human(0, city=self.city, birthYear = self.city.year)
                if len(self.house.residents) < self.house.capacity:
                    human.house = self.house

    def die(self):
        self.city.peopleToKill.append(self)

    #TODO:
    def generateName(self) -> str:
        return "A"