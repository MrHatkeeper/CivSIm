import random
import math
from typing import TYPE_CHECKING

from civsim.Config import Config

if TYPE_CHECKING:
    from civsim.City.City import City

class Human:
    def __init__(self, startAge: int = 0, city: City = None, birthYear: int = None):
        self.name = self.generateName()
        self.age = startAge
        self.hungerRate = Config.HUNGER_RATE.value
        self.happiness = 100
        self.hunger = 0
        self.house = None
        self.isAdult = False
        self.city = city
        self.workplace = None
        self.birthDate = birthYear

    def updateHuman(self):
        self.age = self.city.year - self.birthDate
        if self.age >= Config.ADULT_AGE.value:
            self.isAdult = True
        self.hunger += self.hungerRate
        self.evalHappiness()
        self.killHuman()

    def killHuman(self):
        #TODO: make more complex
        if self.happiness < Config.DEATH_BORDER.value:
            rand = random.randrange(1,100)
            if rand < 50 or self.happiness < 0 or self.hunger >= 10:
                self.city.peopleToKill.append(self)

    def evalHappiness(self):
        if self.house is None:
            self.happiness -= Config.IS_HOUSED_INC.value
        else:
            self.happiness += Config.IS_HOUSED_INC.value

        self.happiness += (self.hunger * -1) * Config.HUNGRY_INC.value + Config.HUNGRY_INC.value
        if self.happiness > 100:
            self.happiness = 100

    def reproduce(self):
        if not self.isAdult:
            return
        partner = None

        if self.house is not None:
            for resident in self.house.residents:
                if resident is not self and resident.isAdult:
                    partner = resident
                    break
        else:
            for human in self.city.population:
                if human is not self and human.isAdult and human.house is None:
                    partner = human
                    break

        if partner is None:
            return
        if id(self) > id(partner):
            return
        base_chance = Config.BIRTH_RATIO.value

        if self.house is not None:
            happiness_factor = (self.happiness + partner.happiness) / 2
            chance = base_chance * (happiness_factor / 100)
        else:
            happiness_factor = (self.happiness + partner.happiness) / 2
            chance = base_chance * Config.HOMELESS_BIRTH_RATIO.value * (happiness_factor / 100)
        if random.random() * 100 < chance:
            baby = Human(0, city=self.city, birthYear=self.city.year)

            baby.house = None
            baby.hunger = (self.hunger + partner.hunger)/2
            if self. house is not None and len(self.house.residents) < self.house.capacity:
                baby.house = self.house
                self.house.residents.append(baby)


            self.city.population.append(baby)


    #TODO:
    def generateName(self) -> str:
        return "A"