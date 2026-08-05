import unittest

from Civsim.City.City import City
from Civsim.City.House import House
from Civsim.City.Workplace.EResources import EResources
from Civsim.City.Workplace.Workplace import Workplace
from Civsim.Human.Human import Human


class TestPopulationSystem(unittest.TestCase):
    def testFeedPopulation(self):
        city = City(0, 3, 0)
        city.storage[EResources.FOOD] = 500
        for human in city.population:
            human.hunger = 5

        city.populationSystem.feedPopulation()
        self.assertEqual(city.storage[EResources.FOOD], 485)

        for human in city.population:
            self.assertEqual(human.hunger, 0)

    def testNotEnoughFoodToFeedPopulation(self):
        city = City(0, 3, 0)
        city.storage[EResources.FOOD] = 4
        city.populationSystem.updatePopulation()
        self.assertEqual(city.storage[EResources.FOOD], 0)

    def testNoFoodInStorage(self):
        city = City(0, 3, 0)
        city.storage[EResources.FOOD] = 0
        city.populationSystem.updatePopulation()
        self.assertEqual(city.storage[EResources.FOOD], 0)

        for human in city.population:
            self.assertEqual(human.hunger != 0, True)

    def testKillPeople(self):
        city = City(0, 3, 0)
        sacrifice = Human(999, city)
        city.population.append(sacrifice)
        house = House()
        sacrifice.house = house
        house.residents.append(sacrifice)
        city.houses.append(sacrifice)

        workplace = Workplace(EResources.FOOD, city)
        workplace.workforce.append(sacrifice)
        sacrifice.workplace = workplace
        city.workplaces.append(workplace)

        city.peopleToKill.append(sacrifice)
        city.populationSystem.killPeople()
        self.assertEqual(len(city.population), 3)
        self.assertEqual(len(house.residents), 0)
        self.assertEqual(len(workplace.workforce), 0)

    def testKillMorePeople(self):
        city = City(0, 3, 0)
        sacrifice1 = Human(20, city)
        sacrifice2 = Human(20, city)
        city.population.append(sacrifice1)
        city.peopleToKill.append(sacrifice1)

        city.population.append(sacrifice2)
        city.peopleToKill.append(sacrifice2)

        city.populationSystem.killPeople()

        self.assertEqual(len(city.population), 3)
