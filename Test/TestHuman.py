import unittest

from Civsim.City.City import City
from Civsim.City.House import House
from Civsim.Human.Human import Human


class TestHuman(unittest.TestCase):
    def testIsAdult(self):
        human = Human(20)
        human.isAdult()
        self.assertTrue(human.adult)

        human = Human(0)
        human.isAdult()
        self.assertFalse(human.adult)

    def testUpdateHuman(self):
        city = City(-2, 0, 0)
        human = Human(20, city, 0)
        city.population.append(human)
        city.updateCity()
        self.assertEqual(human.age, 21)
        human.updateHuman()
        self.assertEqual(human.hunger, human.hungerRate)
        self.assertEqual(human.happiness, 92)

    def testUnderageCanHaveChild(self):
        city = City(-2, 0, 0)
        underage = Human(5, city)
        self.assertEqual(underage.reproduce(), None)

    def testSoloAdultCanHaveChild(self):
        city = City(-2, 0, 0)
        human = Human(20, city, 0)
        city.population.append(human)
        human.adult = True
        self.assertEqual(human.reproduce(), None)

    def testTwoHomelessCanHaveChild(self):
        city = City(-2, 0, 0)
        human1 = Human(20, city)
        human2 = Human(20, city)
        city.population.append(human1)
        city.population.append(human2)
        human1.happiness = 9999999999
        human2.happiness = 9999999999
        human1.adult = True
        human2.adult = True
        if id(human1) > id(human2):
            human2.reproduce()
        else:
            human1.reproduce()
        self.assertEqual(len(city.population), 3)

    def testTwoHousedCanHaveChild(self):
        city = City(-2, 0, 0)
        human1 = Human(20, city)
        human2 = Human(20, city)
        house = House()
        city.houses.append(house)
        house.residents.append(human1)
        house.residents.append(human2)
        city.population.append(human1)
        city.population.append(human2)
        human1.happiness = 9999999999
        human2.happiness = 9999999999
        human1.adult = True
        human2.adult = True
        if id(human1) > id(human2):
            human2.reproduce()
        else:
            human1.reproduce()
        self.assertEqual(len(city.population), 3)

    def testWhenHungryHumanDie(self):
        city = City(-2, 0, 0)
        human = Human(20, city)
        city.population.append(human)
        human.hunger = 99999999
        human.happiness = 29
        human.killHuman()
        self.assertEqual(len(city.peopleToKill), 1)

    def testWhenSadHumanDie(self):
        city = City(-2, 0, 0)
        human = Human(20, city)
        city.population.append(human)
        human.happiness = 0
        human.killHuman()
        self.assertEqual(len(city.peopleToKill), 1)
        
    def testNormalHumanWontDie(self):
        city = City(-2, 0, 0)
        human = Human(20, city)
        human.happiness = 30
        human.killHuman()
        self.assertEqual(len(city.peopleToKill), 0)